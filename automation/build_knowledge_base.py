#!/usr/bin/env python3
"""Build a searchable local knowledge base from WB OpenAPI YAML files."""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml

HTTP_METHODS = ("get", "post", "put", "patch", "delete", "options", "head")


@dataclass(frozen=True)
class Paths:
    repo_root: Path
    indexes_dir: Path
    knowledge_dir: Path


def repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return slug or "section"


def strip_html(value: str) -> str:
    return re.sub(r"<[^>]+>", " ", value or "").replace("&nbsp;", " ").strip()


def normalize_space(value: str) -> str:
    return re.sub(r"\s+", " ", value or "").strip()


def dump_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    with path.open("w", encoding="utf-8", newline="\n") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False) + "\n")


def render_markdown_document(document: dict[str, Any], methods: list[dict[str, Any]]) -> str:
    lines = [
        f"# {document['title']}",
        "",
        f"- Source YAML: `{document['source_file']}`",
        f"- Version: `{document['version']}`",
        f"- Methods: `{document['method_count']}`",
    ]
    if document["domains"]:
        lines.append(f"- Domains: {', '.join(document['domains'])}")
    lines.extend(["", "## Summary", "", document["description"] or "No summary provided.", ""])

    if document["tags"]:
        lines.extend(["## Tags", ""])
        for tag in document["tags"]:
            lines.append(f"- {tag}")
        lines.append("")

    lines.extend(["## Methods", ""])
    for method in methods:
        lines.append(f"### `{method['http_method']} {method['path']}`")
        lines.append("")
        lines.append(f"- Summary: {method['summary'] or 'No summary provided.'}")
        lines.append(f"- Operation ID: `{method['operation_id']}`")
        lines.append(f"- Domain: `{method['domain']}`")
        if method["base_urls"]:
            lines.append(f"- Base URLs: {', '.join(f'`{url}`' for url in method['base_urls'])}")
        if method["tags"]:
            lines.append(f"- Tags: {', '.join(method['tags'])}")
        if method["required_parameters"]:
            lines.append(
                f"- Required parameters: {', '.join(f'`{name}`' for name in method['required_parameters'])}"
            )
        if method["rate_limit_summary"]:
            lines.append(f"- Rate limit hint: {method['rate_limit_summary']}")
        if method["deprecated"]:
            lines.append("- Deprecated: yes")
        if method["readonly"]:
            lines.append("- Read-only: yes")
        if method["sandbox_urls"]:
            lines.append(
                f"- Sandbox URLs: {', '.join(f'`{url}`' for url in method['sandbox_urls'])}"
            )
        lines.extend(["", method["description"] or "No description provided.", ""])
    return "\n".join(lines).strip() + "\n"


def classify_domain(base_urls: list[str], file_slug: str) -> str:
    domain_rules = (
        ("analytics", ("seller-analytics-api",)),
        ("finance", ("finance-api",)),
        ("statistics", ("statistics-api",)),
        ("content", ("content-api",)),
        ("prices", ("discounts-prices-api",)),
        ("communications", ("buyer-chat-api", "feedbacks-api")),
        ("documents", ("documents-api",)),
        ("supplies", ("supplies-api",)),
        ("returns", ("returns-api",)),
        ("advert", ("advert-api",)),
        ("common", ("common-api", "user-management-api")),
        ("marketplace", ("marketplace-api",)),
    )
    for canonical, markers in domain_rules:
        if any(marker in url for marker in markers for url in base_urls):
            return canonical
    if file_slug in {"orders-fbs", "orders-dbw", "orders-dbs", "orders-fbw", "in-store-pickup"}:
        return "marketplace"
    return file_slug


def parse_yaml_file(path: Path) -> tuple[dict[str, Any], list[dict[str, Any]], list[dict[str, Any]], dict[str, Any]]:
    spec = yaml.safe_load(path.read_text(encoding="utf-8"))
    info = spec.get("info", {})
    tags = spec.get("tags", [])
    tag_descriptions = {
        tag.get("name", ""): normalize_space(strip_html(tag.get("description", "")))
        for tag in tags
        if isinstance(tag, dict)
    }
    file_slug = info.get("x-file-name") or path.stem.split("-", 1)[-1]
    methods: list[dict[str, Any]] = []
    auth_rows: list[dict[str, Any]] = []
    document_domains: set[str] = set()
    document_base_urls: set[str] = set()
    document_sandbox_urls: set[str] = set()

    for endpoint_path, operations in (spec.get("paths") or {}).items():
        if not isinstance(operations, dict):
            continue
        path_servers = [server.get("url") for server in operations.get("servers", []) if server.get("url")]
        for http_method, operation in operations.items():
            if http_method not in HTTP_METHODS or not isinstance(operation, dict):
                continue

            operation_servers = [
                server.get("url") for server in operation.get("servers", []) if server.get("url")
            ]
            base_urls = operation_servers or path_servers or []
            sandbox_urls = [url for url in base_urls if "sandbox" in url]
            required_parameters = [
                param.get("name")
                for param in operation.get("parameters", [])
                if isinstance(param, dict) and param.get("required") and param.get("name")
            ]
            response_codes = list((operation.get("responses") or {}).keys())
            description = normalize_space(strip_html(operation.get("description", "")))
            summary = normalize_space(strip_html(operation.get("summary", "")))
            category = operation.get("x-category")
            readonly = bool(operation.get("x-readonly-method"))
            deprecated = bool(operation.get("deprecated"))
            security = operation.get("security", spec.get("security", []))
            domain = classify_domain(base_urls, file_slug)
            document_domains.add(domain)
            document_base_urls.update(base_urls)
            document_sandbox_urls.update(sandbox_urls)
            method_tags = operation.get("tags", [])

            rate_limit_summary = ""
            limit_match = re.search(r"Лимит[^.]+(?:\.|$)", description, re.IGNORECASE)
            if limit_match:
                rate_limit_summary = normalize_space(limit_match.group(0))

            row = {
                "document_slug": file_slug,
                "document_title": info.get("title", file_slug),
                "source_file": path.name,
                "operation_id": operation.get("operationId") or f"{http_method}_{slugify(endpoint_path)}",
                "http_method": http_method.upper(),
                "path": endpoint_path,
                "base_urls": base_urls,
                "sandbox_urls": sandbox_urls,
                "domain": domain,
                "category": category,
                "tags": method_tags,
                "tag_descriptions": {name: tag_descriptions.get(name, "") for name in method_tags},
                "summary": summary,
                "description": description,
                "required_parameters": required_parameters,
                "response_codes": response_codes,
                "response_count": len(response_codes),
                "deprecated": deprecated,
                "readonly": readonly,
                "security": security,
                "rate_limit_summary": rate_limit_summary,
                "search_text": normalize_space(
                    " ".join(
                        [
                            info.get("title", ""),
                            endpoint_path,
                            operation.get("operationId", ""),
                            summary,
                            description,
                            " ".join(method_tags),
                            " ".join(required_parameters),
                            domain,
                            category or "",
                        ]
                    )
                ),
            }
            methods.append(row)

            for security_item in security:
                if not isinstance(security_item, dict):
                    continue
                for scheme_name in security_item.keys():
                    auth_rows.append(
                        {
                            "document_slug": file_slug,
                            "document_title": info.get("title", file_slug),
                            "source_file": path.name,
                            "path": endpoint_path,
                            "http_method": http_method.upper(),
                            "operation_id": row["operation_id"],
                            "scheme": scheme_name,
                            "domain": domain,
                            "base_urls": base_urls,
                        }
                    )

    document_row = {
        "document_slug": file_slug,
        "source_file": path.name,
        "title": info.get("title", file_slug),
        "version": info.get("version", ""),
        "description": normalize_space(strip_html(info.get("description", ""))),
        "tags": [tag.get("name") for tag in tags if isinstance(tag, dict) and tag.get("name")],
        "domains": sorted(document_domains),
        "base_urls": sorted(document_base_urls),
        "sandbox_urls": sorted(document_sandbox_urls),
        "method_count": len(methods),
        "search_text": normalize_space(
            " ".join(
                [
                    info.get("title", ""),
                    info.get("description", ""),
                    " ".join(tag.get("name", "") for tag in tags if isinstance(tag, dict)),
                    file_slug,
                    path.name,
                ]
            )
        ),
    }
    return document_row, methods, auth_rows, spec


def build(paths: Paths) -> dict[str, int]:
    paths.indexes_dir.mkdir(parents=True, exist_ok=True)
    paths.knowledge_dir.mkdir(parents=True, exist_ok=True)

    yaml_files = sorted(paths.repo_root.glob("*.yaml"))
    documents: list[dict[str, Any]] = []
    methods: list[dict[str, Any]] = []
    auth_rows: list[dict[str, Any]] = []
    domain_rows: list[dict[str, Any]] = []

    for yaml_file in yaml_files:
        document_row, doc_methods, doc_auth_rows, _spec = parse_yaml_file(yaml_file)
        documents.append(document_row)
        methods.extend(doc_methods)
        auth_rows.extend(doc_auth_rows)

        grouped_methods = [row for row in doc_methods]
        markdown = render_markdown_document(document_row, grouped_methods)
        (paths.knowledge_dir / f"{document_row['document_slug']}.md").write_text(
            markdown, encoding="utf-8", newline="\n"
        )

    by_domain: dict[str, dict[str, Any]] = {}
    for method in methods:
        current = by_domain.setdefault(
            method["domain"],
            {"domain": method["domain"], "method_count": 0, "base_urls": set(), "documents": set()},
        )
        current["method_count"] += 1
        current["base_urls"].update(method["base_urls"])
        current["documents"].add(method["document_slug"])

    for domain_name, payload in sorted(by_domain.items()):
        domain_rows.append(
            {
                "domain": domain_name,
                "method_count": payload["method_count"],
                "base_urls": sorted(payload["base_urls"]),
                "documents": sorted(payload["documents"]),
            }
        )

    dump_jsonl(paths.indexes_dir / "documents.jsonl", documents)
    dump_jsonl(paths.indexes_dir / "methods.jsonl", methods)
    dump_jsonl(paths.indexes_dir / "auth.jsonl", auth_rows)
    dump_jsonl(paths.indexes_dir / "domains.jsonl", domain_rows)

    return {
        "documents": len(documents),
        "methods": len(methods),
        "auth_rows": len(auth_rows),
        "domains": len(domain_rows),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=str(repo_root()), help="Project root containing *.yaml files")
    parser.add_argument("--indexes-dir", default=None, help="Directory for generated JSONL indexes")
    parser.add_argument("--knowledge-dir", default=None, help="Directory for generated Markdown pages")
    args = parser.parse_args()

    root = Path(args.repo_root).resolve()
    paths = Paths(
        repo_root=root,
        indexes_dir=Path(args.indexes_dir).resolve() if args.indexes_dir else root / "indexes",
        knowledge_dir=Path(args.knowledge_dir).resolve() if args.knowledge_dir else root / "knowledge",
    )
    counts = build(paths)
    print(
        json.dumps(
            {"repo_root": str(paths.repo_root), "indexes_dir": str(paths.indexes_dir), **counts},
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
