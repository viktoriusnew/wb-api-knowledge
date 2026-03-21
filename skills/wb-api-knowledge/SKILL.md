---
name: wb-api-knowledge
description: Use this skill when working with the local Wildberries API knowledge base, especially to find WB Seller API methods from the OpenAPI YAML files, identify the correct domain and base URL, explain authorization and rate-limit hints, compare adjacent sections like orders, reports, analytics, and finances, or answer which endpoint to use for a seller integration task.
---

# WB API Knowledge

This skill answers questions from the bundled Wildberries API knowledge base stored inside the skill itself. It also contains a lightweight bridge to local `n8n` workflow patterns when the user is building WB automations.

Skill root for this installation:

- `C:\Users\viktor\.codex\skills\wb-api-knowledge`

## Workflow

1. Search the bundled index first:
   - `python scripts/search_knowledge.py "<query>"`
   - Use `--kind documents` when the user is asking about a section instead of a method.
   - Use `--domain <name>` when the request clearly targets `common`, `marketplace`, `analytics`, `statistics`, `finance`, `content`, `communications`, `advert`, `supplies`, `returns`, `documents`, or `prices`.
2. Open the bundled Markdown file in `knowledge/` when you need richer context for a section.
3. If the user is building an automation in `n8n`, also open `references/n8n-patterns.md` and combine it with the relevant endpoint details from the indexes.
4. For direct endpoint questions, answer with:
   - HTTP method and path
   - domain and base URL
   - required parameters
   - auth scheme
   - rate-limit hint if present
   - deprecated or sandbox status if present
5. For ambiguous business questions, start from `documents.jsonl` or the section Markdown, then narrow to specific methods.

## Source Priority

Prefer local generated artifacts in this order:

1. `indexes/methods.jsonl` for endpoint lookup
2. `indexes/documents.jsonl` for section lookup
3. `indexes/auth.jsonl` for auth lookup
4. `indexes/domains.jsonl` for domain grouping
5. `knowledge/*.md` for section-level reading
6. Raw `*.yaml` only when the generated artifacts are not enough
7. `references/n8n-patterns.md` only when the user is asking for workflow design or `n8n` implementation shape

## Interpretation Rules

- Treat the bundled indexes and Markdown documents as the canonical source for this installed skill snapshot.
- Prefer path, `operationId`, and tag matches over fuzzy business-language matches.
- If multiple domains look plausible, call that out explicitly and list the strongest candidates.
- When a method is `deprecated`, mention that directly in the answer.
- When sandbox URLs exist, mention them separately from production URLs.
- When the YAML contains rate-limit text inside the description, surface it as a hint rather than inventing stricter rules.
- If a question asks "where to get data" rather than "which method", answer first with the section/domain, then the endpoint candidates.

## Important Files

- `indexes/methods.jsonl`
- `indexes/documents.jsonl`
- `indexes/auth.jsonl`
- `indexes/domains.jsonl`
- `knowledge/`
- `scripts/search_knowledge.py`
- `references/repo-paths.md`
- `references/n8n-patterns.md`

## Useful Commands

- `python scripts/search_knowledge.py "ping"`
- `python scripts/search_knowledge.py "остатки" --kind documents`
- `python scripts/search_knowledge.py "/api/v1/account/balance" --domain finance`

## Notes

- Keep answers concise and integration-oriented.
- Use Russian by default unless the user asks otherwise.
- When n8n templates exist in the repo, prefer extracting their proven patterns instead of inventing workflow structure from scratch.
- Never keep real WB tokens inside reusable workflow JSON or examples; use placeholders or credentials.
- This installed skill is intentionally self-contained so it can work even if the original project folder is removed.
