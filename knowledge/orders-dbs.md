# Заказы DBS

- Source YAML: `05-orders-dbs.yaml`
- Version: `order`
- Methods: `32`
- Domains: marketplace

## Summary

Узнать больше о заказах DBS можно в справочном центре Управление [сборочными заданиями](/openapi/orders-dbs#tag/Sborochnye-zadaniya-DBS) и [метаданными](/openapi/orders-dbs#tag/Metadannye-DBS) заказов DBS (Delivery by Seller).

## Tags

- Сборочные задания DBS
- Метаданные DBS

## Methods

### `GET /api/v3/dbs/orders/new`

- Summary: Получить список новых сборочных заданий
- Operation ID: `get_api-v3-dbs-orders-new`
- Domain: `marketplace`
- Base URLs: `https://marketplace-api.wildberries.ru`
- Tags: Сборочные задания DBS
- Rate limit hint: Лимит запросов на один аккаунт продавца для методов сборочных заданий DBS : | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 мин | 300 запросов | 200 мс | 20 запросов |
- Read-only: yes

Метод возвращает список всех новых [сборочных заданий](/openapi/orders-dbs#tag/Sborochnye-zadaniya-DBS), которые есть у продавца на момент запроса. Лимит запросов на один аккаунт продавца для методов сборочных заданий DBS : | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 мин | 300 запросов | 200 мс | 20 запросов |

### `GET /api/v3/dbs/orders`

- Summary: Получить информацию о завершенных сборочных заданиях
- Operation ID: `get_api-v3-dbs-orders`
- Domain: `marketplace`
- Base URLs: `https://marketplace-api.wildberries.ru`
- Tags: Сборочные задания DBS
- Required parameters: `dateFrom`, `dateTo`
- Rate limit hint: Лимит запросов на один аккаунт продавца для методов сборочных заданий DBS : | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 мин | 300 запросов | 200 мс | 20 запросов |
- Read-only: yes

Метод возвращает информацию о завершенных [сборочных заданиях](/openapi/orders-dbs#tag/Sborochnye-zadaniya-DBS) после продажи или отмены заказа. Можно получить данные за заданный период, максимум 30 календарных дней одним запросом. Лимит запросов на один аккаунт продавца для методов сборочных заданий DBS : | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 мин | 300 запросов | 200 мс | 20 запросов |

### `POST /api/v3/dbs/groups/info`

- Summary: Получить информацию о платной доставке
- Operation ID: `post_api-v3-dbs-groups-info`
- Domain: `marketplace`
- Base URLs: `https://marketplace-api.wildberries.ru`
- Tags: Сборочные задания DBS
- Rate limit hint: Лимит запросов на один аккаунт продавца для методов сборочных заданий DBS : | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 мин | 300 запросов | 200 мс | 20 запросов | Один запрос с кодом ответа 409 учитывается как 10 запросов
- Read-only: yes

Метод возвращает информацию о платной доставке сборочных заданий, которые поступили на один склад (`warehouseId`) в рамках одной транзакции покупателя (`orderUid`). Лимит запросов на один аккаунт продавца для методов сборочных заданий DBS : | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 мин | 300 запросов | 200 мс | 20 запросов | Один запрос с кодом ответа 409 учитывается как 10 запросов

### `POST /api/v3/dbs/orders/client`

- Summary: Информация о покупателе
- Operation ID: `post_api-v3-dbs-orders-client`
- Domain: `marketplace`
- Base URLs: `https://marketplace-api.wildberries.ru`
- Tags: Сборочные задания DBS
- Rate limit hint: Лимит запросов на один аккаунт продавца для методов сборочных заданий DBS : | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 мин | 300 запросов | 200 мс | 20 запросов | Один запрос с кодом ответа 409 учитывается как 10 запросов
- Read-only: yes

Метод возвращает информацию о покупателе по ID сборочных заданий. Лимит запросов на один аккаунт продавца для методов сборочных заданий DBS : | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 мин | 300 запросов | 200 мс | 20 запросов | Один запрос с кодом ответа 409 учитывается как 10 запросов

### `POST /api/marketplace/v3/dbs/orders/b2b/info`

- Summary: Информация о покупателе B2B
- Operation ID: `post_api-marketplace-v3-dbs-orders-b2b-info`
- Domain: `marketplace`
- Base URLs: `https://marketplace-api.wildberries.ru`
- Tags: Сборочные задания DBS
- Rate limit hint: Лимит запросов на один аккаунт продавца для методов сборочных заданий DBS : | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 мин | 300 запросов | 200 мс | 20 запросов |
- Read-only: yes

Метод возвращает данные B2B-покупателей по ID сборочных заданий: - ИНН - КПП - Наименование организации Лимит запросов на один аккаунт продавца для методов сборочных заданий DBS : | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 мин | 300 запросов | 200 мс | 20 запросов |

### `POST /api/v3/dbs/orders/delivery-date`

- Summary: Дата и время доставки
- Operation ID: `post_api-v3-dbs-orders-delivery-date`
- Domain: `marketplace`
- Base URLs: `https://marketplace-api.wildberries.ru`
- Tags: Сборочные задания DBS
- Rate limit hint: Лимит запросов на один аккаунт продавца для методов сборочных заданий DBS : | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 мин | 300 запросов | 200 мс | 20 запросов |
- Read-only: yes

Метод возвращает информацию о выбранных покупателем дате и времени доставки сборочных заданий. Лимит запросов на один аккаунт продавца для методов сборочных заданий DBS : | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 мин | 300 запросов | 200 мс | 20 запросов |

### `POST /api/marketplace/v3/dbs/orders/status/info`

- Summary: Получить статусы сборочных заданий
- Operation ID: `post_api-marketplace-v3-dbs-orders-status-info`
- Domain: `marketplace`
- Base URLs: `https://marketplace-api.wildberries.ru`
- Tags: Сборочные задания DBS
- Rate limit hint: Лимит запросов на один аккаунт продавца для методов сборочных заданий DBS : | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 мин | 300 запросов | 200 мс | 20 запросов |
- Read-only: yes

Метод возвращает статусы [сборочных заданий](/openapi/orders-dbs#tag/Sborochnye-zadaniya-DBS) по их ID. `supplierStatus` — статус сборочного задания. Триггер его изменения — действие самого продавца. Возможные значения `supplierStatus`: | Статус | Описание | Как перевести сборочное задание в данный статус | | ------- | --------- | --------------------------------------| | `new` | **Новое сборочное задание** | | | `confirm` | **На сборке** | [Перевести сборочное задание на сборку](/openapi/orders-dbs#tag/Sborochnye-zadaniya-DBS/paths/~1api~1marketplace~1v3~1dbs~1orders~1status~1confirm/post) | `deliver` | **В доставке** | [Перевести сборочное задание в доставку](/openapi/orders-dbs#tag/Sborochnye-zadaniya-DBS/paths/~1api~1marketplace~1v3~1dbs~1orders~1status~1deliver/post) | `receive` | **Получено покупателем** | [Сообщить, что заказ принят покупателем](/openapi/orders-dbs#tag/Sborochnye-zadaniya-DBS/paths/~1api~1marketplace~1v3~1dbs~1orders~1status~1receive/post) | `reject` | **Отказ покупателя при получении** | [Сообщить, что покупатель отказался от заказа](/openapi/orders-dbs#tag/Sborochnye-zadaniya-DBS/paths/~1api~1marketplace~1v3~1dbs~1orders~1status~1reject/post) | `cancel` | **Отменено продавцом** | [Отменить сборочное задание](/openapi/orders-dbs#tag/Sborochnye-zadaniya-DBS/paths/~1api~1marketplace~1v3~1dbs~1orders~1status~1cancel/post) | `cancel_missed_call` | **Отмена по причине недозвона** | Статус меняется автоматически | `wbStatus` — статус системы Wildberries. Возможные значения `wbStatus`: - `waiting` — сборочное задание в работе - `sold` — заказ получен покупателем - `canceled` — отмена сборочного задания - `canceled_by_client` — покупатель отменил заказ при получении - `declined_by_client` — покупатель отменил заказ в первый чаc Отмена доступна покупателю в первый час с момента заказа, если заказ не переведен на сборку - `defect` — отмена заказа по причине брака - `ready_for_pickup` — сборочное задание прибыло на ПВЗ - `canceled_by_missed_call` — отмена по причине недозвона Лимит запросов на один аккаунт продавца для методов сборочных заданий DBS : | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 мин | 300 запросов | 200 мс | 20 запросов |

### `POST /api/marketplace/v3/dbs/orders/status/cancel`

- Summary: Отменить сборочные задания
- Operation ID: `post_api-marketplace-v3-dbs-orders-status-cancel`
- Domain: `marketplace`
- Base URLs: `https://marketplace-api.wildberries.ru`
- Tags: Сборочные задания DBS
- Rate limit hint: Лимит запросов на один аккаунт продавца: | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 сек | 1 запрос | 1 сек | 10 запросов | Один запрос с кодом ответа 409 учитывается как 10 запросов

Метод переводит [сборочные задания](/openapi/orders-dbs#tag/Sborochnye-zadaniya-DBS) из [статусов](/openapi/orders-dbs#tag/Sborochnye-zadaniya-DBS/paths/~1api~1marketplace~1v3~1dbs~1orders~1status~1info/post) `new`, `confirm` и `deliver` в статус `cancel` — отменено продавцом. Лимит запросов на один аккаунт продавца: | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 сек | 1 запрос | 1 сек | 10 запросов | Один запрос с кодом ответа 409 учитывается как 10 запросов

### `POST /api/marketplace/v3/dbs/orders/status/confirm`

- Summary: Перевести сборочные задания на сборку
- Operation ID: `post_api-marketplace-v3-dbs-orders-status-confirm`
- Domain: `marketplace`
- Base URLs: `https://marketplace-api.wildberries.ru`
- Tags: Сборочные задания DBS
- Rate limit hint: Лимит запросов на один аккаунт продавца: | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 сек | 1 запрос | 1 сек | 10 запросов | Один запрос с кодом ответа 409 учитывается как 10 запросов

Метод переводит [сборочные задания](/openapi/orders-dbs#tag/Sborochnye-zadaniya-DBS) из [статуса](/openapi/orders-dbs#tag/Sborochnye-zadaniya-DBS/paths/~1api~1marketplace~1v3~1dbs~1orders~1status~1info/post) `new` в статус `confirm` — на сборке. Лимит запросов на один аккаунт продавца: | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 сек | 1 запрос | 1 сек | 10 запросов | Один запрос с кодом ответа 409 учитывается как 10 запросов

### `POST /api/marketplace/v3/dbs/orders/stickers`

- Summary: Получить стикеры для сборочных заданий с доставкой в ПВЗ
- Operation ID: `post_api-marketplace-v3-dbs-orders-stickers`
- Domain: `marketplace`
- Base URLs: `https://marketplace-api.wildberries.ru`
- Tags: Сборочные задания DBS
- Required parameters: `type`, `width`, `height`
- Rate limit hint: Лимит запросов на один аккаунт продавца для методов сборочных заданий DBS : | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 мин | 300 запросов | 200 мс | 20 запросов |
- Read-only: yes

Метод доступен по типам токенов : Персональный , Сервисный Метод возвращает стикеры для сборочных заданий с доставкой в ПВЗ в [статусах](/openapi/orders-dbs#tag/Sborochnye-zadaniya-DBS/paths/~1api~1marketplace~1v3~1dbs~1orders~1status~1info/post): - `confirm` — на сборке - `deliver` — в доставке Получить стикеры можно только в размере 580x400 px в формате PDF. Лимит запросов на один аккаунт продавца для методов сборочных заданий DBS : | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 мин | 300 запросов | 200 мс | 20 запросов |

### `POST /api/marketplace/v3/dbs/orders/status/deliver`

- Summary: Перевести сборочные задания в доставку
- Operation ID: `post_api-marketplace-v3-dbs-orders-status-deliver`
- Domain: `marketplace`
- Base URLs: `https://marketplace-api.wildberries.ru`
- Tags: Сборочные задания DBS
- Rate limit hint: Лимит запросов на один аккаунт продавца: | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 сек | 1 запрос | 1 сек | 10 запросов | Один запрос с кодом ответа 409 учитывается как 10 запросов

Метод переводит [сборочные задания](/openapi/orders-dbs#tag/Sborochnye-zadaniya-DBS) из [статуса](/openapi/orders-dbs#tag/Sborochnye-zadaniya-DBS/paths/~1api~1marketplace~1v3~1dbs~1orders~1status~1info/post) `confirm` в статус `deliver` — в доставке. Лимит запросов на один аккаунт продавца: | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 сек | 1 запрос | 1 сек | 10 запросов | Один запрос с кодом ответа 409 учитывается как 10 запросов

### `POST /api/marketplace/v3/dbs/orders/status/receive`

- Summary: Сообщить о получении заказов
- Operation ID: `post_api-marketplace-v3-dbs-orders-status-receive`
- Domain: `marketplace`
- Base URLs: `https://marketplace-api.wildberries.ru`
- Tags: Сборочные задания DBS
- Rate limit hint: Лимит запросов на один аккаунт продавца: | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 сек | 1 запрос | 1 сек | 10 запросов | Один запрос с кодом ответа 409 учитывается как 10 запросов

Метод переводит [сборочные задания](/openapi/orders-dbs#tag/Sborochnye-zadaniya-DBS) из [статуса](/openapi/orders-dbs#tag/Sborochnye-zadaniya-DBS/paths/~1api~1marketplace~1v3~1dbs~1orders~1status~1info/post) `deliver` в статус `receive` — получено покупателем. Лимит запросов на один аккаунт продавца: | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 сек | 1 запрос | 1 сек | 10 запросов | Один запрос с кодом ответа 409 учитывается как 10 запросов

### `POST /api/marketplace/v3/dbs/orders/status/reject`

- Summary: Сообщить об отказе от заказов
- Operation ID: `post_api-marketplace-v3-dbs-orders-status-reject`
- Domain: `marketplace`
- Base URLs: `https://marketplace-api.wildberries.ru`
- Tags: Сборочные задания DBS
- Rate limit hint: Лимит запросов на один аккаунт продавца: | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 сек | 1 запрос | 1 сек | 10 запросов | Один запрос с кодом ответа 409 учитывается как 10 запросов

Метод переводит [сборочные задания](/openapi/orders-dbs#tag/Sborochnye-zadaniya-DBS) из [статуса](/openapi/orders-dbs#tag/Sborochnye-zadaniya-DBS/paths/~1api~1marketplace~1v3~1dbs~1orders~1status~1info/post) `deliver` в статус `reject` — отказ покупателя при получении. Лимит запросов на один аккаунт продавца: | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 сек | 1 запрос | 1 сек | 10 запросов | Один запрос с кодом ответа 409 учитывается как 10 запросов

### `POST /api/v3/dbs/orders/status`

- Summary: Получить статусы сборочных заданий
- Operation ID: `post_api-v3-dbs-orders-status`
- Domain: `marketplace`
- Base URLs: `https://marketplace-api.wildberries.ru`
- Tags: Сборочные задания DBS
- Deprecated: yes
- Read-only: yes

Данный метод устарел. Он будет удалён [13 апреля](https://dev.wildberries.ru/release-notes?id=378)

### `PATCH /api/v3/dbs/orders/{orderId}/cancel`

- Summary: Отменить сборочное задание
- Operation ID: `patch_api-v3-dbs-orders-orderid-cancel`
- Domain: `marketplace`
- Base URLs: `https://marketplace-api.wildberries.ru`
- Tags: Сборочные задания DBS
- Deprecated: yes

Данный метод устарел. Он будет удалён [13 апреля](https://dev.wildberries.ru/release-notes?id=378)

### `PATCH /api/v3/dbs/orders/{orderId}/confirm`

- Summary: Перевести на сборку
- Operation ID: `patch_api-v3-dbs-orders-orderid-confirm`
- Domain: `marketplace`
- Base URLs: `https://marketplace-api.wildberries.ru`
- Tags: Сборочные задания DBS
- Deprecated: yes

Данный метод устарел. Он будет удалён [13 апреля](https://dev.wildberries.ru/release-notes?id=378)

### `PATCH /api/v3/dbs/orders/{orderId}/deliver`

- Summary: Перевести в доставку
- Operation ID: `patch_api-v3-dbs-orders-orderid-deliver`
- Domain: `marketplace`
- Base URLs: `https://marketplace-api.wildberries.ru`
- Tags: Сборочные задания DBS
- Deprecated: yes

Данный метод устарел. Он будет удалён [13 апреля](https://dev.wildberries.ru/release-notes?id=378)

### `PATCH /api/v3/dbs/orders/{orderId}/receive`

- Summary: Сообщить, что заказ принят покупателем
- Operation ID: `patch_api-v3-dbs-orders-orderid-receive`
- Domain: `marketplace`
- Base URLs: `https://marketplace-api.wildberries.ru`
- Tags: Сборочные задания DBS
- Deprecated: yes

Данный метод устарел. Он будет удалён [13 апреля](https://dev.wildberries.ru/release-notes?id=378)

### `PATCH /api/v3/dbs/orders/{orderId}/reject`

- Summary: Сообщить, что покупатель отказался от заказа
- Operation ID: `patch_api-v3-dbs-orders-orderid-reject`
- Domain: `marketplace`
- Base URLs: `https://marketplace-api.wildberries.ru`
- Tags: Сборочные задания DBS
- Deprecated: yes

Данный метод устарел. Он будет удалён [13 апреля](https://dev.wildberries.ru/release-notes?id=378)

### `POST /api/marketplace/v3/dbs/orders/meta/info`

- Summary: Получить метаданные сборочных заданий
- Operation ID: `post_api-marketplace-v3-dbs-orders-meta-info`
- Domain: `marketplace`
- Base URLs: `https://marketplace-api.wildberries.ru`
- Tags: Метаданные DBS
- Rate limit hint: Лимит запросов на один аккаунт продавца для всех методов получения и удаления метаданных DBS : | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 мин | 150 запросов | 400 мс | 20 запросов | Один запрос с кодом ответа 409 учитывается как 10 запросов
- Read-only: yes

Метод возвращает метаданные [сборочных заданий](/openapi/orders-dbs#tag/Sborochnye-zadaniya-DBS). Перечень метаданных, доступных для сборочного задания, можно получить в [списке новых сборочных заданий](/openapi/orders-dbs#tag/Sborochnye-zadaniya-DBS/paths/~1api~1v3~1dbs~1orders~1new/get), поле `requiredMeta`. Возможные метаданные: - `imei` — [IMEI](/openapi/orders-dbs#tag/Metadannye-DBS/paths/~1api~1marketplace~1v3~1dbs~1orders~1meta~1imei/post) - `uin` — [УИН](/openapi/orders-dbs#tag/Metadannye-DBS/paths/~1api~1marketplace~1v3~1dbs~1orders~1meta~1uin/post) - `gtin` — [GTIN](/openapi/orders-dbs#tag/Metadannye-DBS/paths/~1api~1marketplace~1v3~1dbs~1orders~1meta~1gtin/post) - `sgtin` — [код маркировки](/openapi/orders-dbs#tag/Metadannye-DBS/paths/~1api~1marketplace~1v3~1dbs~1orders~1meta~1sgtin/post) - `customsDeclaration` — [номер ГТД](/openapi/orders-dbs#tag/Metadannye-DBS/paths/~1api~1marketplace~1v3~1dbs~1meta~1customs-declaration/post) Если ответ вернулся с пустой структурой `meta`, значит у сборочного задания нет метаданных и добавить их нельзя. Лимит запросов на один аккаунт продавца для всех методов получения и удаления метаданных DBS : | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 мин | 150 запросов | 400 мс | 20 запросов | Один запрос с кодом ответа 409 учитывается как 10 запросов

### `POST /api/marketplace/v3/dbs/orders/meta/delete`

- Summary: Удалить метаданные сборочных заданий
- Operation ID: `post_api-marketplace-v3-dbs-orders-meta-delete`
- Domain: `marketplace`
- Base URLs: `https://marketplace-api.wildberries.ru`
- Tags: Метаданные DBS
- Rate limit hint: Лимит запросов на один аккаунт продавца для всех методов получения и удаления метаданных DBS : | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 мин | 150 запросов | 400 мс | 20 запросов | Один запрос с кодом ответа 409 учитывается как 10 запросов

Метод удаляет значение указанных [метаданных](/openapi/orders-dbs#tag/Metadannye-DBS/paths/~1api~1marketplace~1v3~1dbs~1orders~1meta~1info/post) для нескольких сборочных заданий. В одном запросе можно удалить метаданные только одного типа. Укажите тип метаданных в запросе: - `imei` — [IMEI](/openapi/orders-dbs#tag/Metadannye-DBS/paths/~1api~1marketplace~1v3~1dbs~1orders~1meta~1imei/post) - `uin` — [УИН](/openapi/orders-dbs#tag/Metadannye-DBS/paths/~1api~1marketplace~1v3~1dbs~1orders~1meta~1uin/post) - `gtin` — [GTIN](/openapi/orders-dbs#tag/Metadannye-DBS/paths/~1api~1marketplace~1v3~1dbs~1orders~1meta~1gtin/post) - `sgtin` — [код маркировки](/openapi/orders-dbs#tag/Metadannye-DBS/paths/~1api~1marketplace~1v3~1dbs~1orders~1meta~1sgtin/post) - `customsDeclaration` — [номер ГТД](/openapi/orders-dbs#tag/Metadannye-DBS/paths/~1api~1marketplace~1v3~1dbs~1meta~1customs-declaration/post) Лимит запросов на один аккаунт продавца для всех методов получения и удаления метаданных DBS : | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 мин | 150 запросов | 400 мс | 20 запросов | Один запрос с кодом ответа 409 учитывается как 10 запросов

### `POST /api/marketplace/v3/dbs/orders/meta/sgtin`

- Summary: Закрепить коды маркировки за сборочными заданиями
- Operation ID: `post_api-marketplace-v3-dbs-orders-meta-sgtin`
- Domain: `marketplace`
- Base URLs: `https://marketplace-api.wildberries.ru`
- Tags: Метаданные DBS
- Rate limit hint: Лимит запросов на один аккаунт продавца для всех методов закрепления метаданных DBS : | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 мин | 500 запросов | 120 мс | 20 запросов | Один запрос с кодом ответа 409 учитывается как 10 запросов

Метод обновляет код маркировки [Честный знак](https://честныйзнак.рф/) в [метаданных](/openapi/orders-dbs#tag/Metadannye-DBS/paths/~1api~1marketplace~1v3~1dbs~1orders~1meta~1info/post) нескольких сборочных заданий. Закрепить код маркировки можно, только если в [метаданных сборочного задания](/openapi/orders-dbs#tag/Metadannye-DBS/paths/~1api~1marketplace~1v3~1dbs~1orders~1meta~1info/post) есть поле `sgtin`, а сборочное задание находится в [статусе](/openapi/orders-dbs#tag/Sborochnye-zadaniya-DBS/paths/~1api~1marketplace~1v3~1dbs~1orders~1status~1info/post) `confirm` — на сборке. Получить загруженные маркировки можно в [метаданных сборочного задания](/openapi/orders-dbs#tag/Metadannye-DBS/paths/~1api~1marketplace~1v3~1dbs~1orders~1meta~1info/post). Лимит запросов на один аккаунт продавца для всех методов закрепления метаданных DBS : | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 мин | 500 запросов | 120 мс | 20 запросов | Один запрос с кодом ответа 409 учитывается как 10 запросов

### `POST /api/marketplace/v3/dbs/orders/meta/uin`

- Summary: Закрепить УИН за сборочными заданиями
- Operation ID: `post_api-marketplace-v3-dbs-orders-meta-uin`
- Domain: `marketplace`
- Base URLs: `https://marketplace-api.wildberries.ru`
- Tags: Метаданные DBS
- Rate limit hint: Лимит запросов на один аккаунт продавца для всех методов закрепления метаданных DBS : | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 мин | 500 запросов | 120 мс | 20 запросов | Один запрос с кодом ответа 409 учитывается как 10 запросов

Метод обновляет УИН, уникальный идентификационный номер, в [метаданных сборочных заданий](/openapi/orders-dbs#tag/Metadannye-DBS/paths/~1api~1marketplace~1v3~1dbs~1orders~1meta~1info/post). У одного сборочного задания может быть только один УИН. Добавлять УИН можно только для сборочных заданий, которые доставляются WB и находятся в [статусе](/openapi/orders-dbs#tag/Sborochnye-zadaniya-DBS/paths/~1api~1marketplace~1v3~1dbs~1orders~1status~1info/post) `confirm`. Лимит запросов на один аккаунт продавца для всех методов закрепления метаданных DBS : | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 мин | 500 запросов | 120 мс | 20 запросов | Один запрос с кодом ответа 409 учитывается как 10 запросов

### `POST /api/marketplace/v3/dbs/orders/meta/imei`

- Summary: Закрепить IMEI за сборочными заданиями
- Operation ID: `post_api-marketplace-v3-dbs-orders-meta-imei`
- Domain: `marketplace`
- Base URLs: `https://marketplace-api.wildberries.ru`
- Tags: Метаданные DBS
- Rate limit hint: Лимит запросов на один аккаунт продавца для всех методов закрепления метаданных DBS : | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 мин | 500 запросов | 120 мс | 20 запросов | Один запрос с кодом ответа 409 учитывается как 10 запросов

Метод обновляет IMEI в [метаданных](/openapi/orders-dbs#tag/Metadannye-DBS/paths/~1api~1marketplace~1v3~1dbs~1orders~1meta~1info/post) нескольких сборочных заданий. У одного сборочного задания может быть только один IMEI. Добавлять IMEI можно только для сборочных заданий, которые доставляются WB и находятся в [статусе](/openapi/orders-dbs#tag/Sborochnye-zadaniya-DBS/paths/~1api~1marketplace~1v3~1dbs~1orders~1status~1info/post) `confirm`. Лимит запросов на один аккаунт продавца для всех методов закрепления метаданных DBS : | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 мин | 500 запросов | 120 мс | 20 запросов | Один запрос с кодом ответа 409 учитывается как 10 запросов

### `POST /api/marketplace/v3/dbs/orders/meta/gtin`

- Summary: Закрепить GTIN за сборочными заданиями
- Operation ID: `post_api-marketplace-v3-dbs-orders-meta-gtin`
- Domain: `marketplace`
- Base URLs: `https://marketplace-api.wildberries.ru`
- Tags: Метаданные DBS
- Rate limit hint: Лимит запросов на один аккаунт продавца для всех методов закрепления метаданных DBS : | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 мин | 500 запросов | 120 мс | 20 запросов | Один запрос с кодом ответа 409 учитывается как 10 запросов

Метод обновляет GTIN, уникальный ID товара в Беларуси, в [метаданных](/openapi/orders-dbs#tag/Metadannye-DBS/paths/~1api~1marketplace~1v3~1dbs~1orders~1meta~1info/post) нескольких сборочных заданий. У одного сборочного задания может быть только один GTIN. Добавлять GTIN можно только для сборочных заданий, которые доставляются WB и находятся в [статусе](/openapi/orders-dbs#tag/Sborochnye-zadaniya-DBS/paths/~1api~1marketplace~1v3~1dbs~1orders~1status~1info/post) `confirm`. Лимит запросов на один аккаунт продавца для всех методов закрепления метаданных DBS : | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 мин | 500 запросов | 120 мс | 20 запросов | Один запрос с кодом ответа 409 учитывается как 10 запросов

### `POST /api/marketplace/v3/dbs/orders/meta/customs-declaration`

- Summary: Закрепить за сборочными заданиями номер ГТД
- Operation ID: `post_api-marketplace-v3-dbs-orders-meta-customs-declaration`
- Domain: `marketplace`
- Base URLs: `https://marketplace-api.wildberries.ru`
- Tags: Метаданные DBS
- Rate limit hint: Лимит запросов на один аккаунт продавца для всех методов закрепления метаданных DBS : | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 мин | 500 запросов | 120 мс | 20 запросов | Один запрос с кодом ответа 409 учитывается как 10 запросов

Метод обновляет номер ГТД — грузовой таможенной декларации — в [метаданных сборочных заданий](/openapi/orders-dbs#tag/Metadannye-DBS/paths/~1api~1marketplace~1v3~1dbs~1orders~1meta~1info/post). У одного сборочного задания может быть только один ГТД. Добавлять номер ГТД можно только для сборочных заданий, которые находятся в [статусе](/openapi/orders-dbs#tag/Sborochnye-zadaniya-DBS/paths/~1api~1v3~1dbs~1orders~1status/post) `deliver`. Лимит запросов на один аккаунт продавца для всех методов закрепления метаданных DBS : | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 мин | 500 запросов | 120 мс | 20 запросов | Один запрос с кодом ответа 409 учитывается как 10 запросов

### `GET /api/v3/dbs/orders/{orderId}/meta`

- Summary: Получить метаданные сборочного задания
- Operation ID: `get_api-v3-dbs-orders-orderid-meta`
- Domain: `marketplace`
- Base URLs: `https://marketplace-api.wildberries.ru`
- Tags: Метаданные DBS
- Deprecated: yes
- Read-only: yes

Данный метод устарел. Он будет удалён [13 апреля](https://dev.wildberries.ru/release-notes?id=378)

### `DELETE /api/v3/dbs/orders/{orderId}/meta`

- Summary: Удалить метаданные сборочного задания
- Operation ID: `delete_api-v3-dbs-orders-orderid-meta`
- Domain: `marketplace`
- Base URLs: `https://marketplace-api.wildberries.ru`
- Tags: Метаданные DBS
- Deprecated: yes

Данный метод устарел. Он будет удалён [13 апреля](https://dev.wildberries.ru/release-notes?id=378)

### `PUT /api/v3/dbs/orders/{orderId}/meta/sgtin`

- Summary: Закрепить за сборочным заданием код маркировки товара
- Operation ID: `put_api-v3-dbs-orders-orderid-meta-sgtin`
- Domain: `marketplace`
- Base URLs: `https://marketplace-api.wildberries.ru`
- Tags: Метаданные DBS
- Deprecated: yes

Данный метод устарел. Он будет удалён [13 апреля](https://dev.wildberries.ru/release-notes?id=378)

### `PUT /api/v3/dbs/orders/{orderId}/meta/uin`

- Summary: Закрепить за сборочным заданием УИН (уникальный идентификационный номер)
- Operation ID: `put_api-v3-dbs-orders-orderid-meta-uin`
- Domain: `marketplace`
- Base URLs: `https://marketplace-api.wildberries.ru`
- Tags: Метаданные DBS
- Deprecated: yes

Данный метод устарел. Он будет удалён [13 апреля](https://dev.wildberries.ru/release-notes?id=378)

### `PUT /api/v3/dbs/orders/{orderId}/meta/imei`

- Summary: Закрепить за сборочным заданием IMEI
- Operation ID: `put_api-v3-dbs-orders-orderid-meta-imei`
- Domain: `marketplace`
- Base URLs: `https://marketplace-api.wildberries.ru`
- Tags: Метаданные DBS
- Deprecated: yes

Данный метод устарел. Он будет удалён [13 апреля](https://dev.wildberries.ru/release-notes?id=378)

### `PUT /api/v3/dbs/orders/{orderId}/meta/gtin`

- Summary: Закрепить за сборочным заданием GTIN
- Operation ID: `put_api-v3-dbs-orders-orderid-meta-gtin`
- Domain: `marketplace`
- Base URLs: `https://marketplace-api.wildberries.ru`
- Tags: Метаданные DBS
- Deprecated: yes

Данный метод устарел. Он будет удалён [13 апреля](https://dev.wildberries.ru/release-notes?id=378)
