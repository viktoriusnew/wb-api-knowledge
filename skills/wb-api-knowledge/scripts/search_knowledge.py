#!/usr/bin/env python3
"""Search the bundled WB API knowledge-base indexes inside this skill."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any


def skill_root() -> Path:
    return Path(__file__).resolve().parents[1]


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    with path.open("r", encoding="utf-8") as handle:
        return [json.loads(line) for line in handle if line.strip()]


def tokenize(value: str) -> list[str]:
    return [token for token in re.split(r"[^a-zA-Zа-яА-Я0-9/_-]+", value.lower()) if token]


def score_row(row: dict[str, Any], query: str) -> int:
    haystack = row.get("search_text", "").lower()
    query_lower = query.lower()
    score = 0
    if query_lower in haystack:
        score += 15
    for token in tokenize(query):
        if token in haystack:
            score += 4
        if token == row.get("domain", "").lower():
            score += 3
        if row.get("path", "").lower().startswith(token):
            score += 2
    if query_lower == row.get("operation_id", "").lower():
        score += 10
    if query_lower == row.get("path", "").lower():
        score += 12
    return score


def search(rows: list[dict[str, Any]], query: str, kind: str, limit: int, domain: str | None) -> list[dict[str, Any]]:
    if domain:
        rows = [row for row in rows if row.get("domain") == domain or domain in row.get("domains", [])]
    ranked: list[tuple[int, dict[str, Any]]] = []
    for row in rows:
        score = score_row(row, query)
        if score > 0:
            ranked.append((score, row))
    ranked.sort(key=lambda item: (-item[0], item[1].get("path", item[1].get("document_slug", ""))))
    return [row for _, row in ranked[:limit]]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("query", help="Text, path, or operationId to search for")
    parser.add_argument("--kind", choices=("methods", "documents", "auth", "domains"), default="methods")
    parser.add_argument("--limit", type=int, default=10)
    parser.add_argument("--domain", default=None)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    indexes_path = skill_root() / "indexes" / f"{args.kind}.jsonl"
    rows = load_jsonl(indexes_path)
    results = search(rows, args.query, args.kind, args.limit, args.domain)

    if args.json:
        print(json.dumps(results, ensure_ascii=False, indent=2))
        return 0

    for row in results:
        if args.kind == "methods":
            print(f"[{row['domain']}] {row['http_method']} {row['path']}")
            print(f"  {row['summary']}")
            print(f"  file={row['source_file']} operationId={row['operation_id']}")
        elif args.kind == "documents":
            print(f"[{','.join(row['domains'])}] {row['title']} ({row['source_file']})")
            print(f"  methods={row['method_count']} tags={', '.join(row['tags'])}")
        elif args.kind == "auth":
            print(f"[{row['domain']}] {row['http_method']} {row['path']} -> {row['scheme']}")
        else:
            print(f"{row['domain']}: methods={row['method_count']} documents={', '.join(row['documents'])}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
