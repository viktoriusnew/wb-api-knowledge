import json
import subprocess
import sys
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


def run_build() -> None:
    subprocess.run(
        [sys.executable, "-m", "automation.build_knowledge_base"],
        cwd=REPO_ROOT,
        check=True,
        text=True,
        capture_output=True,
    )


def load_jsonl(name: str) -> list[dict]:
    path = REPO_ROOT / "indexes" / f"{name}.jsonl"
    with path.open("r", encoding="utf-8") as handle:
        return [json.loads(line) for line in handle if line.strip()]


class KnowledgeBaseTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        run_build()

    def test_builds_document_index_for_all_yaml_files(self) -> None:
        documents = load_jsonl("documents")
        self.assertEqual(len(documents), 13)
        self.assertTrue(any(row["document_slug"] == "general" for row in documents))

    def test_contains_ping_method(self) -> None:
        methods = load_jsonl("methods")
        ping_rows = [row for row in methods if row["path"] == "/ping"]
        self.assertTrue(ping_rows)
        self.assertTrue(any("common-api.wildberries.ru" in " ".join(row["base_urls"]) for row in ping_rows))

    def test_contains_deprecated_endpoint(self) -> None:
        methods = load_jsonl("methods")
        deprecated_rows = [row for row in methods if row["deprecated"]]
        self.assertTrue(deprecated_rows)
        self.assertTrue(any(row["path"] == "/api/v1/supplier/incomes" for row in deprecated_rows))

    def test_generates_knowledge_markdown(self) -> None:
        knowledge_path = REPO_ROOT / "knowledge" / "general.md"
        self.assertTrue(knowledge_path.exists())
        self.assertIn("## Methods", knowledge_path.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
