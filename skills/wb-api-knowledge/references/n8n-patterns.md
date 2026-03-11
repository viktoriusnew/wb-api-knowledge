# n8n Patterns For WB API

Практические паттерны ниже извлечены из локальных workflow-шаблонов:

- `WB Test — Проверка ответа Statistics API.json`
- `WB Analytics → Google Sheets.json`
- `WB Analytics2 → Google Sheets.json`

Используй этот файл, когда пользователь просит не просто найти endpoint WB API, а собрать или объяснить автоматизацию для `n8n`, особенно вместе с `Google Sheets`.

## Повторяющиеся паттерны

### 1. Trigger -> Dates -> WB API

Базовый стартовый шаблон:

1. `Manual Trigger` для ручного прогона или `Schedule Trigger` для cron.
2. `Code`-нода, которая готовит:
   - `date_from`
   - `date_to`
   - RFC-подобные строки вроде `2026-02-17T00:00:00%2B03:00`
   - `past_date`
   - дополнительные диапазоны вроде `stocks_date_from`
3. `HTTP Request`-ноды к WB API, которые используют значения из `Code Dates`.

Практический вывод:

- Для WB-интеграций полезно централизовать дату в одной `Code`-ноде, а не дублировать вычисления по всем HTTP-запросам.
- Для статистики и аналитики удобно сразу готовить и обычную дату `yyyy-MM-dd`, и строку с часовым поясом `+03:00`.

### 2. Один кабинет -> несколько WB API -> merge

Шаблоны показывают паттерн для одного кабинета:

- `seller-analytics-api` для метрик карточек и продаж
- `advert-api` для рекламных расходов и промо-позиций
- `statistics-api` для выкупов, продаж и остатков

Дальше ответы собираются через `Merge` и дообрабатываются в `Code`.

Практический вывод:

- Когда метрика не покрывается одним endpoint, строй workflow как агрегатор нескольких WB API.
- Для кабинетов или брендов удобнее дублировать связку нод на каждый кабинет, а затем объединять результаты.

### 3. Google Sheets как источник входных nmId

Во втором шаблоне `Google Sheets` используется не только как приёмник, но и как источник списка карточек:

- чтение диапазона через Google Sheets API
- `Code Parse Cards` превращает строки в массив `cards`
- из строк выделяются `nmIds`
- `nmIds` подставляются в аналитический запрос WB

Практический вывод:

- Для точечных отчётов по карточкам удобный паттерн: `Sheets Read -> Parse -> nmIds -> WB Analytics`.
- Если пользователь просит "взять список карточек из таблицы", это уже готовый подтверждённый паттерн из живых workflow.

### 4. HTTP Request к WB API

Подтверждённые паттерны запросов:

- `POST https://seller-analytics-api.wildberries.ru/api/analytics/v3/sales-funnel/products`
- `GET https://statistics-api.wildberries.ru/api/v5/supplier/reportDetailByPeriod`
- `GET https://statistics-api.wildberries.ru/api/v1/supplier/stocks`
- `GET https://advert-api.wildberries.ru/adv/v1/upd`

Типовая схема:

- `Authorization` header
- `Content-Type: application/json` для POST
- query params через expression для дат
- JSON body через expression, когда набор `nmIds` формируется динамически

Практический вывод:

- Для WB в n8n чаще всего нужен `HTTP Request`, а не специализированный node.
- Лучше собирать `jsonBody` и query parameters из expression-значений, а не хардкодить статические даты.

### 5. Code-ноды как слой нормализации

Шаблоны активно используют `Code`-ноды для:

- объединения ответов из разных API
- расчёта бизнес-метрик
- нормализации массива ответов
- преобразования строк Google Sheets в объекты карточек
- подготовки `batchUpdate` payload для Google Sheets

Практический вывод:

- Для WB+n8n хороший дизайн: `HTTP Request` отвечает только за вызов API, а бизнес-логику и маппинг лучше держать в `Code`.
- Если пользователь просит "готовый workflow", допустимо закладывать 1-3 `Code`-ноды между WB и Sheets.

### 6. Google Sheets batchUpdate

Оба шаблона пишут в Google Sheets через `values:batchUpdate`, а не по одной ячейке.

Практический вывод:

- Для массивной записи метрик предпочитай один `batchUpdate` вместо множества отдельных операций.
- Перед записью удобно подготовить массив `data: [{ range, values }]` в `Code`-ноде.

### 7. Частичное обогащение карточек

Во втором шаблоне поверх analytics добавляются:

- остатки
- количество отзывов
- количество вопросов
- рекламная позиция/поисковая позиция

Практический вывод:

- Для карточечных отчётов есть хороший композиционный паттерн:
  `cards from Sheets -> analytics -> feedbacks/questions -> stocks -> advert -> merge -> write back`.

## Что брать как recommended default

Если пользователь просит построить n8n-автоматизацию на WB API и не задаёт архитектуру явно, используй такой базовый шаблон:

1. `Manual Trigger` или `Schedule Trigger`
2. `Code Dates`
3. Один или несколько `HTTP Request` к WB API
4. `Code` для нормализации и объединения
5. При необходимости `Merge`
6. `HTTP Request` к Google Sheets `values:batchUpdate` или официальный Google Sheets node

## Важные замечания

- Не копируй токены из шаблонов в новые workflow; используй credentials или плейсхолдеры.
- Если пользователь зовёт одновременно `n8n-skill` и `wb-api-knowledge`, этот файл использовать как bridge между знанием WB API и формой n8n workflow.
- Для простого поиска endpoint этот файл не нужен; он нужен именно для интеграционных сценариев.
