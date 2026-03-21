# Заказы Самовывоз

- Source YAML: `06-in-store-pickup.yaml`
- Version: `instorepickup`
- Methods: `28`
- Domains: marketplace

## Summary

Управление [сборочными заданиями](/openapi/in-store-pickup#tag/Sborochnye-zadaniya-Samovyvoz) и [метаданными](/openapi/in-store-pickup#tag/Metadannye-Samovyvoz) заказов модели Самовывоз.

## Tags

- Сборочные задания Самовывоз
- Метаданные Самовывоз

## Methods

### `GET /api/v3/click-collect/orders/new`

- Summary: Получить список новых сборочных заданий
- Operation ID: `get_api-v3-click-collect-orders-new`
- Domain: `marketplace`
- Tags: Сборочные задания Самовывоз
- Rate limit hint: Лимит запросов на один аккаунт продавца для методов сборочных заданий Самовывоз : | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 мин | 300 запросов | 200 мс | 20 запросов | Один запрос с кодом ответа 409 учитывается как 10 запросов
- Read-only: yes

Метод возвращает список всех новых [сборочных заданий](/openapi/in-store-pickup#tag/Sborochnye-zadaniya-Samovyvoz), которые есть у продавца на момент запроса. Лимит запросов на один аккаунт продавца для методов сборочных заданий Самовывоз : | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 мин | 300 запросов | 200 мс | 20 запросов | Один запрос с кодом ответа 409 учитывается как 10 запросов

### `POST /api/marketplace/v3/click-collect/orders/status/confirm`

- Summary: Перевести сборочные задания на сборку
- Operation ID: `post_api-marketplace-v3-click-collect-orders-status-confirm`
- Domain: `marketplace`
- Tags: Сборочные задания Самовывоз
- Rate limit hint: Лимит запросов на один аккаунт продавца для методов сборочных заданий Самовывоз : | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 сек | 1 запрос | 1 сек | 10 запросов | Один запрос с кодом ответа 409 учитывается как 10 запросов

Метод переводит [сборочные задания](/openapi/in-store-pickup#tag/Sborochnye-zadaniya-Samovyvoz) из [статуса](/openapi/in-store-pickup#tag/Sborochnye-zadaniya-Samovyvoz/paths/~1api~1marketplace~1v3~1click-collect~1orders~1status~1info/post) `new` — новый — в статус `confirm` — на сборке. Лимит запросов на один аккаунт продавца для методов сборочных заданий Самовывоз : | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 сек | 1 запрос | 1 сек | 10 запросов | Один запрос с кодом ответа 409 учитывается как 10 запросов

### `POST /api/marketplace/v3/click-collect/orders/status/prepare`

- Summary: Сообщить, что сборочные задания готовы к выдаче
- Operation ID: `post_api-marketplace-v3-click-collect-orders-status-prepare`
- Domain: `marketplace`
- Tags: Сборочные задания Самовывоз
- Rate limit hint: Лимит запросов на один аккаунт продавца для методов сборочных заданий Самовывоз : | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 сек | 1 запрос | 1 сек | 10 запросов | Один запрос с кодом ответа 409 учитывается как 10 запросов

Метод переводит [сборочные задания](/openapi/in-store-pickup#tag/Sborochnye-zadaniya-Samovyvoz) из [статуса](/openapi/in-store-pickup#tag/Sborochnye-zadaniya-Samovyvoz/paths/~1api~1marketplace~1v3~1click-collect~1orders~1status~1info/post) `confirm` — на сборке — в статус `prepare` — готово к выдаче. Лимит запросов на один аккаунт продавца для методов сборочных заданий Самовывоз : | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 сек | 1 запрос | 1 сек | 10 запросов | Один запрос с кодом ответа 409 учитывается как 10 запросов

### `PATCH /api/v3/click-collect/orders/{orderId}/confirm`

- Summary: Перевести на сборку
- Operation ID: `patch_api-v3-click-collect-orders-orderid-confirm`
- Domain: `marketplace`
- Tags: Сборочные задания Самовывоз
- Required parameters: `orderId`
- Deprecated: yes

Данный метод устарел. Он будет удалён [19 мая](https://dev.wildberries.ru/release-notes?id=474)

### `PATCH /api/v3/click-collect/orders/{orderId}/prepare`

- Summary: Сообщить, что сборочное задание готово к выдаче
- Operation ID: `patch_api-v3-click-collect-orders-orderid-prepare`
- Domain: `marketplace`
- Tags: Сборочные задания Самовывоз
- Required parameters: `orderId`
- Deprecated: yes

Данный метод устарел. Он будет удалён [19 мая](https://dev.wildberries.ru/release-notes?id=474)

### `POST /api/v3/click-collect/orders/client`

- Summary: Информация о покупателе
- Operation ID: `post_api-v3-click-collect-orders-client`
- Domain: `marketplace`
- Tags: Сборочные задания Самовывоз
- Rate limit hint: Лимит запросов на один аккаунт продавца для методов сборочных заданий Самовывоз : | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 мин | 300 запросов | 200 мс | 20 запросов | Один запрос с кодом ответа 409 учитывается как 10 запросов
- Read-only: yes

Метод возвращает информацию о покупателе по ID сборочного задания. Доступно только для сборочных заданий в статусах: - `confirm` — на сборке - `prepare` — готов к выдаче Лимит запросов на один аккаунт продавца для методов сборочных заданий Самовывоз : | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 мин | 300 запросов | 200 мс | 20 запросов | Один запрос с кодом ответа 409 учитывается как 10 запросов

### `POST /api/v3/click-collect/orders/client/identity`

- Summary: Проверить, что заказ принадлежит покупателю
- Operation ID: `post_api-v3-click-collect-orders-client-identity`
- Domain: `marketplace`
- Tags: Сборочные задания Самовывоз
- Rate limit hint: Лимит запросов на один аккаунт продавца: | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 мин | 30 запросов | 2 сек | 20 запросов | Один запрос с кодом ответа 409 учитывается как 10 запросов
- Read-only: yes

Метод сообщает, принадлежит ли проверяемый заказ покупателю или нет по переданному коду. Доступно, если хотя бы одно сборочное задание из заказа находится в статусе prepare - готов к выдаче. Лимит запросов на один аккаунт продавца: | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 мин | 30 запросов | 2 сек | 20 запросов | Один запрос с кодом ответа 409 учитывается как 10 запросов

### `POST /api/marketplace/v3/click-collect/orders/status/receive`

- Summary: Сообщить, что заказы приняты покупателями
- Operation ID: `post_api-marketplace-v3-click-collect-orders-status-receive`
- Domain: `marketplace`
- Tags: Сборочные задания Самовывоз
- Rate limit hint: Лимит запросов на один аккаунт продавца для методов сборочных заданий Самовывоз : | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 сек | 1 запрос | 1 сек | 10 запросов | Один запрос с кодом ответа 409 учитывается как 10 запросов

Метод переводит [сборочные задания](/openapi/in-store-pickup#tag/Sborochnye-zadaniya-Samovyvoz) из [статуса](/openapi/in-store-pickup#tag/Sborochnye-zadaniya-Samovyvoz/paths/~1api~1marketplace~1v3~1click-collect~1orders~1status~1info/post) `prepare` — готово к выдаче — в статус `receive` — получено покупателем. Лимит запросов на один аккаунт продавца для методов сборочных заданий Самовывоз : | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 сек | 1 запрос | 1 сек | 10 запросов | Один запрос с кодом ответа 409 учитывается как 10 запросов

### `POST /api/marketplace/v3/click-collect/orders/status/reject`

- Summary: Сообщить об отказе от заказов
- Operation ID: `post_api-marketplace-v3-click-collect-orders-status-reject`
- Domain: `marketplace`
- Tags: Сборочные задания Самовывоз
- Rate limit hint: Лимит запросов на один аккаунт продавца для методов сборочных заданий Самовывоз : | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 сек | 1 запрос | 1 сек | 10 запросов | Один запрос с кодом ответа 409 учитывается как 10 запросов

Метод переводит [сборочные задания](/openapi/in-store-pickup#tag/Sborochnye-zadaniya-Samovyvoz) из [статуса](/openapi/in-store-pickup#tag/Sborochnye-zadaniya-Samovyvoz/paths/~1api~1marketplace~1v3~1click-collect~1orders~1status~1info/post) `prepare` — готово к выдаче — в статус `reject` — отказ при получении. Лимит запросов на один аккаунт продавца для методов сборочных заданий Самовывоз : | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 сек | 1 запрос | 1 сек | 10 запросов | Один запрос с кодом ответа 409 учитывается как 10 запросов

### `PATCH /api/v3/click-collect/orders/{orderId}/receive`

- Summary: Сообщить, что заказ принят покупателем
- Operation ID: `patch_api-v3-click-collect-orders-orderid-receive`
- Domain: `marketplace`
- Tags: Сборочные задания Самовывоз
- Required parameters: `orderId`
- Deprecated: yes

Данный метод устарел. Он будет удалён [19 мая](https://dev.wildberries.ru/release-notes?id=474)

### `PATCH /api/v3/click-collect/orders/{orderId}/reject`

- Summary: Сообщить, что покупатель отказался от заказа
- Operation ID: `patch_api-v3-click-collect-orders-orderid-reject`
- Domain: `marketplace`
- Tags: Сборочные задания Самовывоз
- Required parameters: `orderId`
- Deprecated: yes

Данный метод устарел. Он будет удалён [19 мая](https://dev.wildberries.ru/release-notes?id=474)

### `POST /api/marketplace/v3/click-collect/orders/status/info`

- Summary: Получить статусы сборочных заданий
- Operation ID: `post_api-marketplace-v3-click-collect-orders-status-info`
- Domain: `marketplace`
- Tags: Сборочные задания Самовывоз
- Rate limit hint: Лимит запросов на один аккаунт продавца для методов сборочных заданий Самовывоз : | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 сек | 1 запрос | 1 сек | 10 запросов | Один запрос с кодом ответа 409 учитывается как 10 запросов
- Read-only: yes

Метод возвращает статусы [сборочных заданий](/openapi/in-store-pickup#tag/Sborochnye-zadaniya-Samovyvoz) по их ID. `supplierStatus` — статус сборочного задания. Триггер его изменения - действие самого продавца. Возможные значения `supplierStatus`: | Статус | Описание | Как перевести сборочное задание в данный статус | | ------- | --------- | --------------------------------------| | `new` | **Новое сборочное задание** | | `confirm` | **На сборке** | [Перевести сборочное задание на сборку](/openapi/in-store-pickup#tag/Sborochnye-zadaniya-Samovyvoz/paths/~1api~1marketplace~1v3~1click-collect~1orders~1status~1confirm/post) | `prepare` | **Готов к выдаче** | [Сообщить, что сборочное задание готово к выдаче](/openapi/in-store-pickup#tag/Sborochnye-zadaniya-Samovyvoz/paths/~1api~1marketplace~1v3~1click-collect~1orders~1status~1prepare/post) | `receive` | **Получено покупателем** | [Сообщить, что заказ принят покупателем](/openapi/in-store-pickup#tag/Sborochnye-zadaniya-Samovyvoz/paths/~1api~1marketplace~1v3~1click-collect~1orders~1status~1receive/post) | `reject` | **Отказ покупателя при получении** | [Сообщить, что покупатель отказался от заказа](/openapi/in-store-pickup#tag/Sborochnye-zadaniya-Samovyvoz/paths/~1api~1marketplace~1v3~1click-collect~1orders~1status~1reject/post) | `cancel` | **Отменено продавцом** | [Отменить сборочное задание](/openapi/in-store-pickup#tag/Sborochnye-zadaniya-Samovyvoz/paths/~1api~1marketplace~1v3~1click-collect~1orders~1status~1cancel/post) | `cancel_shelf_life` | **Отмена по истечении срока хранения** | Переводится автоматически по возникновению события `wbStatus` — статус системы Wildberries. Возможные значения `wbStatus`: - `waiting` - сборочное задание в работе - `sold` - заказ получен покупателем - `canceled` - отмена сборочного задания - `canceled_by_client` - покупатель отменил заказ при получении - `declined_by_client` - покупатель отменил заказ в первый чаc Отмена доступна покупателю в первый час с момента заказа, если заказ не переведён на сборку - `defect` - отмена заказа по причине брака - `ready_for_pickup` - сборочное задание готово к выдаче Лимит запросов на один аккаунт продавца для методов сборочных заданий Самовывоз : | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 сек | 1 запрос | 1 сек | 10 запросов | Один запрос с кодом ответа 409 учитывается как 10 запросов

### `POST /api/v3/click-collect/orders/status`

- Summary: Получить статусы сборочных заданий
- Operation ID: `post_api-v3-click-collect-orders-status`
- Domain: `marketplace`
- Tags: Сборочные задания Самовывоз
- Deprecated: yes
- Read-only: yes

Данный метод устарел. Он будет удалён [19 мая](https://dev.wildberries.ru/release-notes?id=474)

### `GET /api/v3/click-collect/orders`

- Summary: Получить информацию о завершённых сборочных заданиях
- Operation ID: `get_api-v3-click-collect-orders`
- Domain: `marketplace`
- Tags: Сборочные задания Самовывоз
- Required parameters: `limit`, `next`, `dateFrom`, `dateTo`
- Rate limit hint: Лимит запросов на один аккаунт продавца для методов сборочных заданий Самовывоз : | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 мин | 300 запросов | 200 мс | 20 запросов | Один запрос с кодом ответа 409 учитывается как 10 запросов
- Read-only: yes

Метод возвращает информацию о завершённых сборочных заданиях после продажи или отмены заказа. Можно получить данные за заданный период, максимум 30 календарных дней одним запросом. Лимит запросов на один аккаунт продавца для методов сборочных заданий Самовывоз : | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 мин | 300 запросов | 200 мс | 20 запросов | Один запрос с кодом ответа 409 учитывается как 10 запросов

### `POST /api/marketplace/v3/click-collect/orders/status/cancel`

- Summary: Отменить сборочные задания
- Operation ID: `post_api-marketplace-v3-click-collect-orders-status-cancel`
- Domain: `marketplace`
- Tags: Сборочные задания Самовывоз
- Rate limit hint: Лимит запросов на один аккаунт продавца для методов сборочных заданий Самовывоз : | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 сек | 1 запрос | 1 сек | 10 запросов | Один запрос с кодом ответа 409 учитывается как 10 запросов

Переводит [сборочные задания](/openapi/in-store-pickup#tag/Sborochnye-zadaniya-Samovyvoz) из [статусов](/openapi/in-store-pickup#tag/Sborochnye-zadaniya-Samovyvoz/paths/~1api~1marketplace~1v3~1click-collect~1orders~1status~1info/post) `new`, `confirm`, `prepare` в статус `cancel` — отменено продавцом. Лимит запросов на один аккаунт продавца для методов сборочных заданий Самовывоз : | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 сек | 1 запрос | 1 сек | 10 запросов | Один запрос с кодом ответа 409 учитывается как 10 запросов

### `PATCH /api/v3/click-collect/orders/{orderId}/cancel`

- Summary: Отменить сборочное задание
- Operation ID: `patch_api-v3-click-collect-orders-orderid-cancel`
- Domain: `marketplace`
- Tags: Сборочные задания Самовывоз
- Required parameters: `orderId`
- Deprecated: yes

Данный метод устарел. Он будет удалён [19 мая](https://dev.wildberries.ru/release-notes?id=474)

### `POST /api/marketplace/v3/click-collect/orders/meta/info`

- Summary: Получить метаданные сборочных заданий
- Operation ID: `post_api-marketplace-v3-click-collect-orders-meta-info`
- Domain: `marketplace`
- Tags: Метаданные Самовывоз
- Rate limit hint: Лимит запросов на один аккаунт продавца для всех методов получения и удаления метаданных Самовывоз : | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 мин | 150 запросов | 400 мс | 20 запросов | Один запрос с кодом ответа 409 учитывается как 10 запросов
- Read-only: yes

Метод возвращает метаданные [сборочных заданий](/openapi/in-store-pickup#tag/Sborochnye-zadaniya-Samovyvoz). Перечень метаданных, доступных для сборочного задания, можно получить в [списке новых сборочных заданий](/openapi/in-store-pickup#tag/Sborochnye-zadaniya-Samovyvoz/paths/~1api~1v3~1click-collect~1orders~1new/get), поле `requiredMeta`. Лимит запросов на один аккаунт продавца для всех методов получения и удаления метаданных Самовывоз : | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 мин | 150 запросов | 400 мс | 20 запросов | Один запрос с кодом ответа 409 учитывается как 10 запросов

### `POST /api/marketplace/v3/click-collect/orders/meta/delete`

- Summary: Удалить метаданные сборочных заданий
- Operation ID: `post_api-marketplace-v3-click-collect-orders-meta-delete`
- Domain: `marketplace`
- Tags: Метаданные Самовывоз
- Rate limit hint: Лимит запросов на один аккаунт продавца для всех методов получения и удаления метаданных Самовывоз : | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 мин | 150 запросов | 400 мс | 20 запросов | Один запрос с кодом ответа 409 учитывается как 10 запросов

Метод удаляет значения указанных [метаданных](/openapi/in-store-pickup#tag/Metadannye-Samovyvoz/paths/~1api~1marketplace~1v3~1click-collect~1orders~1meta~1info/post) для нескольких сборочных заданий. Одним запросом можно удалить метаданные только одного типа: `imei`, `uin`, `gtin` или `sgtin`. Лимит запросов на один аккаунт продавца для всех методов получения и удаления метаданных Самовывоз : | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 мин | 150 запросов | 400 мс | 20 запросов | Один запрос с кодом ответа 409 учитывается как 10 запросов

### `POST /api/marketplace/v3/click-collect/orders/meta/sgtin`

- Summary: Закрепить коды маркировки товара за сборочными заданиями
- Operation ID: `post_api-marketplace-v3-click-collect-orders-meta-sgtin`
- Domain: `marketplace`
- Tags: Метаданные Самовывоз
- Rate limit hint: Лимит запросов на один аккаунт продавца для всех методов закрепления метаданных Самовывоз : | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 мин | 20 запросов | 3 сек | 500 запросов | Один запрос с кодом ответа 409 учитывается как 10 запросов

Метод обновляет код маркировки [Честный знак](https://честныйзнак.рф/) в [метаданных](/openapi/in-store-pickup#tag/Metadannye-Samovyvoz/paths/~1api~1marketplace~1v3~1click-collect~1orders~1meta~1info/post) нескольких сборочных заданий. Закрепить код маркировки можно, только если в [метаданных сборочного задания](/openapi/in-store-pickup#tag/Metadannye-Samovyvoz/paths/~1api~1marketplace~1v3~1click-collect~1orders~1meta~1info/post) есть поле `sgtin`, а сборочное задание находится в [статусе](/openapi/in-store-pickup#tag/Sborochnye-zadaniya-Samovyvoz/paths/~1api~1marketplace~1v3~1click-collect~1orders~1status~1info/post) `confirm`. Получить загруженные маркировки можно в [метаданных сборочного задания](/openapi/in-store-pickup#tag/Metadannye-Samovyvoz/paths/~1api~1marketplace~1v3~1click-collect~1orders~1meta~1info/post). Лимит запросов на один аккаунт продавца для всех методов закрепления метаданных Самовывоз : | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 мин | 20 запросов | 3 сек | 500 запросов | Один запрос с кодом ответа 409 учитывается как 10 запросов

### `POST /api/marketplace/v3/click-collect/orders/meta/uin`

- Summary: Закрепить УИН за сборочными заданиями
- Operation ID: `post_api-marketplace-v3-click-collect-orders-meta-uin`
- Domain: `marketplace`
- Tags: Метаданные Самовывоз
- Rate limit hint: Лимит запросов на один аккаунт продавца для всех методов закрепления метаданных Самовывоз : | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 мин | 20 запросов | 3 сек | 500 запросов | Один запрос с кодом ответа 409 учитывается как 10 запросов

Метод обновляет УИН, уникальные идентификационные номера, в [метаданных сборочных заданий](/openapi/in-store-pickup#tag/Metadannye-Samovyvoz/paths/~1api~1marketplace~1v3~1click-collect~1orders~1meta~1info/post). У одного сборочного задания может быть только один УИН. Добавлять УИН можно только для сборочных заданий в [статусе](/openapi/in-store-pickup#tag/Sborochnye-zadaniya-Samovyvoz/paths/~1api~1marketplace~1v3~1click-collect~1orders~1status~1info/post) `confirm` и доставка которых осуществляется силами WB. Лимит запросов на один аккаунт продавца для всех методов закрепления метаданных Самовывоз : | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 мин | 20 запросов | 3 сек | 500 запросов | Один запрос с кодом ответа 409 учитывается как 10 запросов

### `POST /api/marketplace/v3/click-collect/orders/meta/imei`

- Summary: Закрепить IMEI за сборочными заданиями
- Operation ID: `post_api-marketplace-v3-click-collect-orders-meta-imei`
- Domain: `marketplace`
- Tags: Метаданные Самовывоз
- Rate limit hint: Лимит запросов на один аккаунт продавца для всех методов закрепления метаданных Самовывоз : | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 мин | 20 запросов | 3 сек | 500 запросов | Один запрос с кодом ответа 409 учитывается как 10 запросов

Метод обновляет IMEI в [метаданных сборочных заданий](/openapi/in-store-pickup#tag/Metadannye-Samovyvoz/paths/~1api~1marketplace~1v3~1click-collect~1orders~1meta~1info/post). У одного сборочного задания может быть только один IMEI. Добавлять IMEI можно только для сборочных заданий в [статусе](/openapi/in-store-pickup#tag/Sborochnye-zadaniya-Samovyvoz/paths/~1api~1marketplace~1v3~1click-collect~1orders~1status~1info/post) `confirm`, если их доставка осуществляется силами WB. Лимит запросов на один аккаунт продавца для всех методов закрепления метаданных Самовывоз : | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 мин | 20 запросов | 3 сек | 500 запросов | Один запрос с кодом ответа 409 учитывается как 10 запросов

### `POST /api/marketplace/v3/click-collect/orders/meta/gtin`

- Summary: Закрепить GTIN за сборочными заданиями
- Operation ID: `post_api-marketplace-v3-click-collect-orders-meta-gtin`
- Domain: `marketplace`
- Tags: Метаданные Самовывоз
- Rate limit hint: Лимит запросов на один аккаунт продавца для всех методов закрепления метаданных Самовывоз : | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 мин | 20 запросов | 3 сек | 500 запросов | Один запрос с кодом ответа 409 учитывается как 10 запросов

Метод обновляет GTIN, уникальный ID товара в Беларуси, в [метаданных](/openapi/in-store-pickup#tag/Metadannye-Samovyvoz/paths/~1api~1marketplace~1v3~1click-collect~1orders~1meta~1info/post) нескольких сборочных заданий. У одного сборочного задания может быть только один GTIN. Добавлять GTIN можно только для сборочных заданий в [статусе](/openapi/in-store-pickup#tag/Sborochnye-zadaniya-Samovyvoz/paths/~1api~1marketplace~1v3~1click-collect~1orders~1status~1info/post) `confirm` и доставка которых осуществляется силами WB. Лимит запросов на один аккаунт продавца для всех методов закрепления метаданных Самовывоз : | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 мин | 20 запросов | 3 сек | 500 запросов | Один запрос с кодом ответа 409 учитывается как 10 запросов

### `GET /api/v3/click-collect/orders/{orderId}/meta`

- Summary: Получить метаданные сборочного задания
- Operation ID: `get_api-v3-click-collect-orders-orderid-meta`
- Domain: `marketplace`
- Tags: Метаданные Самовывоз
- Required parameters: `orderId`
- Deprecated: yes
- Read-only: yes

Данный метод устарел. Он будет удалён [19 мая](https://dev.wildberries.ru/release-notes?id=474)

### `DELETE /api/v3/click-collect/orders/{orderId}/meta`

- Summary: Удалить метаданные сборочного задания
- Operation ID: `delete_api-v3-click-collect-orders-orderid-meta`
- Domain: `marketplace`
- Tags: Метаданные Самовывоз
- Required parameters: `orderId`, `key`
- Deprecated: yes

Данный метод устарел. Он будет удалён [19 мая](https://dev.wildberries.ru/release-notes?id=474)

### `PUT /api/v3/click-collect/orders/{orderId}/meta/sgtin`

- Summary: Закрепить за сборочным заданием код маркировки товара
- Operation ID: `put_api-v3-click-collect-orders-orderid-meta-sgtin`
- Domain: `marketplace`
- Tags: Метаданные Самовывоз
- Required parameters: `orderId`
- Deprecated: yes

Данный метод устарел. Он будет удалён [19 мая](https://dev.wildberries.ru/release-notes?id=474)

### `PUT /api/v3/click-collect/orders/{orderId}/meta/uin`

- Summary: Закрепить за сборочным заданием УИН (уникальный идентификационный номер)
- Operation ID: `put_api-v3-click-collect-orders-orderid-meta-uin`
- Domain: `marketplace`
- Tags: Метаданные Самовывоз
- Required parameters: `orderId`
- Deprecated: yes

Данный метод устарел. Он будет удалён [19 мая](https://dev.wildberries.ru/release-notes?id=474)

### `PUT /api/v3/click-collect/orders/{orderId}/meta/imei`

- Summary: Закрепить за сборочным заданием IMEI
- Operation ID: `put_api-v3-click-collect-orders-orderid-meta-imei`
- Domain: `marketplace`
- Tags: Метаданные Самовывоз
- Required parameters: `orderId`
- Deprecated: yes

Данный метод устарел. Он будет удалён [19 мая](https://dev.wildberries.ru/release-notes?id=474)

### `PUT /api/v3/click-collect/orders/{orderId}/meta/gtin`

- Summary: Закрепить за сборочным заданием GTIN
- Operation ID: `put_api-v3-click-collect-orders-orderid-meta-gtin`
- Domain: `marketplace`
- Tags: Метаданные Самовывоз
- Required parameters: `orderId`
- Deprecated: yes

Данный метод устарел. Он будет удалён [19 мая](https://dev.wildberries.ru/release-notes?id=474)
