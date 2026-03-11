# wb-api-knowledge

Локальная база знаний и навык Codex app для работы с Wildberries API.

Проект собирает searchable knowledge base из OpenAPI YAML-файлов WB API и предоставляет skill `wb-api-knowledge` для локального использования в Codex app. База знаний подходит для быстрого поиска методов, доменов, базовых URL, требований к авторизации, deprecated-методов и соседних разделов API.

В репозитории также могут лежать реальные n8n workflow-шаблоны, из которых skill может брать практические интеграционные паттерны для связки `WB API + n8n + Google Sheets`.

## Что внутри

- исходные OpenAPI YAML по разделам WB API
- генератор базы знаний в `automation/`
- индексы поиска в `indexes/`
- нормализованные Markdown-страницы в `knowledge/`
- skill-источник в `skills/wb-api-knowledge/`
- тесты сборки knowledge base в `tests/`
- локальные n8n workflow-примеры для прикладных паттернов

## Структура

```text
automation/              Скрипты сборки, поиска и установки skill
indexes/                 JSONL-индексы методов, документов, auth и доменов
knowledge/               Нормализованные Markdown-документы по разделам API
skills/wb-api-knowledge/ Исходная версия навыка для Codex app
tests/                   Проверки сборки knowledge base
*.yaml                   Исходные OpenAPI-спецификации Wildberries API
```

## Быстрый старт

Установить зависимости:

```bash
python -m pip install -r requirements.txt
```

Собрать knowledge base:

```bash
python -m automation.build_knowledge_base
```

Найти метод или раздел:

```bash
python -m automation.search_knowledge "ping"
python -m automation.search_knowledge "остатки" --kind documents
python -m automation.search_knowledge "/api/v1/account/balance" --domain finance
```

Установить skill в локальный Codex app:

```bash
python -m automation.install_skill
```

Прогнать тесты:

```bash
python -m unittest discover -s tests -v
```

## Что умеет skill

Навык `wb-api-knowledge` помогает:

- найти endpoint по path, названию или бизнес-задаче
- определить нужный домен и base URL
- быстро понять auth-схему и обязательные параметры
- увидеть deprecated и sandbox-варианты
- различать близкие разделы WB API: заказы, отчёты, аналитика, финансы и другие

## Замечания

- Исходным источником истины считаются OpenAPI YAML в корне проекта.
- Сгенерированные индексы и Markdown-файлы можно пересобирать после обновления YAML.
- GitHub-репозиторий нужен как резервная и передаваемая копия; рантайм навыка остаётся локальным в Codex app.
- Если добавляете workflow-шаблоны n8n, не храните в них реальные токены WB API; используйте credentials или плейсхолдеры.
