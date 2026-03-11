---
name: wb-api-knowledge
description: Use this skill when working with the local Wildberries API knowledge base, especially to find WB Seller API methods from the OpenAPI YAML files, identify the correct domain and base URL, explain authorization and rate-limit hints, compare adjacent sections like orders, reports, analytics, and finances, or answer which endpoint to use for a seller integration task.
---

# WB API Knowledge

This skill answers questions from the local Wildberries API knowledge base that is built from the OpenAPI YAML files in this repo.

Repo root for this installation:

- `C:\Users\viktor\Documents\projects\WB API`

## Workflow

1. Rebuild the local indexes if they are missing or stale:
   - `python -m automation.build_knowledge_base`
2. Search the local index first:
   - `python -m automation.search_knowledge "<query>"`
   - Use `--kind documents` when the user is asking about a section instead of a method.
   - Use `--domain <name>` when the request clearly targets `common`, `marketplace`, `analytics`, `statistics`, `finance`, `content`, `communications`, `advert`, `supplies`, `returns`, `documents`, or `prices`.
3. Open the generated Markdown file in `knowledge/` when you need richer context for a section.
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

## Interpretation Rules

- Treat the OpenAPI YAML files in this repo as the canonical source.
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
- `references/repo-paths.md`

## Useful Commands

- `python -m automation.build_knowledge_base`
- `python -m automation.search_knowledge "ping"`
- `python -m automation.search_knowledge "остатки" --kind documents`
- `python -m automation.search_knowledge "/api/v1/account/balance" --domain finance`
- `python -m unittest discover -s tests -v`

## Notes

- Keep answers concise and integration-oriented.
- Use Russian by default unless the user asks otherwise.
- Do not invent n8n or Google Sheets recipes in this skill version unless the user asks for a custom solution outside the skill.
