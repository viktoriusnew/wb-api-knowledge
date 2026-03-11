# Отчёты

- Source YAML: `12-reports.yaml`
- Version: `reports`
- Methods: `26`
- Domains: analytics, statistics

## Summary

Узнать больше об отчётах можно в справочном центре С помощью этих методов вы можете получить [основные отчёты](/openapi/reports#tag/Osnovnye-otchyoty) и отчёты о: 1. [Остатках на складах](/openapi/reports#tag/Otchyot-ob-ostatkah-na-skladah) 2. [Товарах с обязательной маркировкой](/openapi/reports#tag/Otchyot-o-tovarah-c-obyazatelnoj-markirovkoj) 3. [Удержаниях](/openapi/reports#tag/Otchyoty-ob-uderzhaniyah) 4. [Платной приёмке](/openapi/reports#tag/Platnaya-priyomka) 5. [Платном хранении](/openapi/reports#tag/Platnoe-hranenie) 6. [Продажах по регионам](/openapi/reports#tag/Prodazhi-po-regionam) 7. [Доле бренда в продажах](/openapi/reports#tag/Dolya-brenda-v-prodazhah) 8. [Скрытых товарах](/openapi/reports#tag/Skrytye-tovary) 9. [Возвратах и перемещении товаров](/openapi/reports#tag/Otchyot-o-vozvratah-i-peremeshenii-tovarov)

## Tags

- Основные отчёты
- Отчёт об остатках на складах
- Отчёт о товарах c обязательной маркировкой
- Отчёты об удержаниях
- Платная приёмка
- Платное хранение
- Продажи по регионам
- Доля бренда в продажах
- Скрытые товары
- Отчёт о возвратах и перемещении товаров

## Methods

### `GET /api/v1/supplier/incomes`

- Summary: Поставки
- Operation ID: `get_api-v1-supplier-incomes`
- Domain: `statistics`
- Base URLs: `https://statistics-api.wildberries.ru`
- Tags: Основные отчёты
- Required parameters: `dateFrom`
- Deprecated: yes
- Read-only: yes

Данный метод устарел. Он будет удалён [11 марта](https://dev.wildberries.ru/release-notes?id=431)

### `GET /api/v1/supplier/stocks`

- Summary: Склады
- Operation ID: `get_api-v1-supplier-stocks`
- Domain: `statistics`
- Base URLs: `https://statistics-api.wildberries.ru`
- Tags: Основные отчёты
- Required parameters: `dateFrom`
- Rate limit hint: Лимит запросов на один аккаунт продавца: | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 минута | 1 запрос | 1 минута | 1 запрос |
- Read-only: yes

Метод возвращает остатки товаров на складах WB. Данные этого отчёта могут обновляться с задержкой в несколько часов относительно реальных изменений Не рекомендуем использовать данный отчёт для оперативного переключения между FBW и FBS логистикой. Для контроля актуальных остатков используйте [Отчёт об остатках на складах](/openapi/reports#tag/Otchyot-ob-ostatkah-na-skladah). Сервис не хранит историю наличия товаров на складах, поэтому вы можете получить данные об остатках только в режиме реального времени. Для одного ответа в системе установлено условное ограничение 60000 строк. Поэтому, чтобы получить все остатки, может потребоваться более, чем один запрос. Во втором и далее запросе в параметре `dateFrom` используйте полное значение поля `lastChangeDate` из последней строки ответа на предыдущий запрос. Если в ответе отдаётся пустой массив `[]`, все остатки уже выгружены. Лимит запросов на один аккаунт продавца: | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 минута | 1 запрос | 1 минута | 1 запрос |

### `GET /api/v1/supplier/orders`

- Summary: Заказы
- Operation ID: `get_api-v1-supplier-orders`
- Domain: `statistics`
- Base URLs: `https://statistics-api.wildberries.ru`
- Tags: Основные отчёты
- Required parameters: `dateFrom`
- Rate limit hint: Лимит запросов на один аккаунт продавца: | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 минута | 1 запрос | 1 минута | 1 запрос |
- Read-only: yes

Метод возвращает информацию о заказах. Данные обновляются раз в 30 минут. 1 строка = 1 заказ = 1 сборочное задание = 1 единица товара. Для определения заказа рекомендуем использовать поле `srid`. Информация о заказе хранится 90 дней с момента оформления. В ответах могут отсутствовать заказы, по которым не подтверждена оплата. Например, заказы с отложенными платежами или оплатой в рассрочку. При этом, если по таким заказам есть продажи, вы можете получить их с помощью [детализаций к отчётам реализации](/openapi/financial-reports-and-accounting#tag/Finansovye-otchyoty/paths/~1api~1v5~1supplier~1reportDetailByPeriod/get). Чтобы получить все оформленные заказы, используйте [Ленту заказов](https://seller.wildberries.ru/content-analytics/order-feed) в личном кабинете. Данные этого отчёта являются предварительными и служат для оперативного мониторинга Для одного ответа на запрос с `flag=0` или без `flag` в системе установлено условное ограничение 80000 строк. Поэтому, чтобы получить все заказы, может потребоваться более, чем один запрос. Во втором и далее запросе в параметре `dateFrom` используйте полное значение поля `lastChangeDate` из последней строки ответа на предыдущий запрос. Если в ответе отдаётся пустой массив `[]`, все заказы уже выгружены. Лимит запросов на один аккаунт продавца: | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 минута | 1 запрос | 1 минута | 1 запрос |

### `GET /api/v1/supplier/sales`

- Summary: Продажи
- Operation ID: `get_api-v1-supplier-sales`
- Domain: `statistics`
- Base URLs: `https://statistics-api.wildberries.ru`
- Tags: Основные отчёты
- Required parameters: `dateFrom`
- Rate limit hint: Лимит запросов на один аккаунт продавца: | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 минута | 1 запрос | 1 минута | 1 запрос |
- Read-only: yes

Метод возвращает информацию о продажах и возвратах. Данные обновляются раз в 30 минут. 1 строка = 1 заказ = 1 сборочное задание = 1 единица товара. Для определения заказа рекомендуем использовать поле `srid`. Информация о заказе хранится 90 дней с момента оформления. Данные этого отчёта являются предварительными и служат для оперативного мониторинга - В ответах могут отсутствовать заказы, по которым не подтверждена оплата, даже если эти заказы есть в детализациях к отчётам реализации. Например, заказы с отложенными платежами или оплатой в рассрочку - Значения полей `priceWithDisc` и `forPay` рассчитываются по упрощённой логике и могут отличаться от `retail_price_withdisc_rub` и `ppvz_for_pay` соответственно в детализациях к отчётам реализации - Поля `finishedPrice`, `priceWithDisc`, `forPay` могут временно иметь значение `0`: данные заполняются асинхронно, актуализируются в течение 24 часов - Для заказов, которые оплачены в валюте, отличной от валюты продавца, возможны округления цен из-за конвертации валют Для точных финансовых расчётов, сверки и отчётности используйте [детализации к отчётам реализации](/openapi/financial-reports-and-accounting#tag/Finansovye-otchyoty/paths/~1api~1v5~1supplier~1reportDetailByPeriod/get). Для одного ответа на запрос с `flag=0` или без `flag` в системе установлено условное ограничение 80000 строк. Поэтому, чтобы получить все продажи и возвраты, может потребоваться более, чем один запрос. Во втором и далее запросе в параметре `dateFrom `используйте полное значение поля `lastChangeDate` из последней строки ответа на предыдущий запрос. Если в ответе отдаётся пустой массив `[]`, все продажи и возвраты уже выгружены. Лимит запросов на один аккаунт продавца: | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 минута | 1 запрос | 1 минута | 1 запрос |

### `POST /api/v1/analytics/excise-report`

- Summary: Получить отчёт
- Operation ID: `post_api-v1-analytics-excise-report`
- Domain: `analytics`
- Base URLs: `https://seller-analytics-api.wildberries.ru`
- Tags: Отчёт о товарах c обязательной маркировкой
- Rate limit hint: Лимит запросов на один аккаунт продавца: | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 5 ч | 10 запросов | 30 мин | 10 запросов |
- Read-only: yes

Метод возвращает отчёт с [операциями по товарам с обязательной маркировкой](https://seller.wildberries.ru/analytics-reports/excise-report). Данный отчёт можно сохранить в [формате таблиц](https://dev.wildberries.ru/cases/1). Лимит запросов на один аккаунт продавца: | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 5 ч | 10 запросов | 30 мин | 10 запросов |

### `GET /api/v1/warehouse_remains`

- Summary: Создать отчёт
- Operation ID: `get_api-v1-warehouse-remains`
- Domain: `analytics`
- Base URLs: `https://seller-analytics-api.wildberries.ru`
- Tags: Отчёт об остатках на складах
- Rate limit hint: Лимит запросов на один аккаунт продавца: | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 мин | 1 запрос | 1 мин | 5 запросов |
- Read-only: yes

Метод создаёт [задание на генерацию](/openapi/reports#tag/Otchyot-ob-ostatkah-na-skladah/paths/~1api~1v1~1warehouse_remains~1tasks~1%7Btask_id%7D~1status/get) отчёта об [остатках на складах WB](/openapi/reports#tag/Otchyot-ob-ostatkah-na-skladah/paths/~1api~1v1~1warehouse_remains~1tasks~1%7Btask_id%7D~1download/get). Параметры `groupBy` и `filter` (группировки и фильтры) можно задать в любой комбинации — аналогично [версии](https://seller.wildberries.ru/analytics-reports/warehouse-remains) в личном кабинете. Лимит запросов на один аккаунт продавца: | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 мин | 1 запрос | 1 мин | 5 запросов |

### `GET /api/v1/warehouse_remains/tasks/{task_id}/status`

- Summary: Проверить статус
- Operation ID: `get_api-v1-warehouse-remains-tasks-task-id-status`
- Domain: `analytics`
- Base URLs: `https://seller-analytics-api.wildberries.ru`
- Tags: Отчёт об остатках на складах
- Required parameters: `task_id`
- Rate limit hint: Лимит запросов на один аккаунт продавца: | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 5 сек | 1 запрос | 5 сек | 5 запросов |
- Read-only: yes

Метод возвращает статус [задания на генерацию](/openapi/reports#tag/Otchyot-ob-ostatkah-na-skladah/paths/~1api~1v1~1warehouse_remains/get) отчёта об [остатках на складах WB](/openapi/reports#tag/Otchyot-ob-ostatkah-na-skladah/paths/~1api~1v1~1warehouse_remains~1tasks~1%7Btask_id%7D~1download/get). Лимит запросов на один аккаунт продавца: | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 5 сек | 1 запрос | 5 сек | 5 запросов |

### `GET /api/v1/warehouse_remains/tasks/{task_id}/download`

- Summary: Получить отчёт
- Operation ID: `get_api-v1-warehouse-remains-tasks-task-id-download`
- Domain: `analytics`
- Base URLs: `https://seller-analytics-api.wildberries.ru`
- Tags: Отчёт об остатках на складах
- Required parameters: `task_id`
- Rate limit hint: Лимит запросов на один аккаунт продавца: | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 мин | 1 запрос | 1 мин | 1 запрос |
- Read-only: yes

Метод возвращает отчёт об [остатках на складах WB](https://seller.wildberries.ru/analytics-reports/warehouse-remains) по ID [задания на генерацию](/openapi/reports#tag/Otchyot-ob-ostatkah-na-skladah/paths/~1api~1v1~1warehouse_remains/get). Лимит запросов на один аккаунт продавца: | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 мин | 1 запрос | 1 мин | 1 запрос |

### `GET /api/analytics/v1/measurement-penalties`

- Summary: Удержания за занижение габаритов упаковки
- Operation ID: `getMeasurementPenalties`
- Domain: `analytics`
- Base URLs: `https://seller-analytics-api.wildberries.ru`
- Tags: Отчёты об удержаниях
- Required parameters: `dateTo`, `limit`
- Rate limit hint: Лимит запросов на один аккаунт продавца: | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 мин | 1 запрос | 1 мин | 1 запрос |
- Read-only: yes

Метод возвращает отчёт об [удержаниях за занижение габаритов упаковки](https://seller.wildberries.ru/analytics-reports/dimensions-penalties) Лимит запросов на один аккаунт продавца: | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 мин | 1 запрос | 1 мин | 1 запрос |

### `GET /api/analytics/v1/warehouse-measurements`

- Summary: Замеры склада
- Operation ID: `getWarehouseMeasurements`
- Domain: `analytics`
- Base URLs: `https://seller-analytics-api.wildberries.ru`
- Tags: Отчёты об удержаниях
- Required parameters: `dateTo`, `limit`
- Rate limit hint: Лимит запросов на один аккаунт продавца: | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 мин | 1 запрос | 1 мин | 1 запрос |
- Read-only: yes

Метод возвращает отчёт о [замерах склада](https://seller.wildberries.ru/analytics-reports/dimensions-penalties/warehouse-measurements) Лимит запросов на один аккаунт продавца: | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 мин | 1 запрос | 1 мин | 1 запрос |

### `GET /api/analytics/v1/deductions`

- Summary: Подмены и неверные вложения
- Operation ID: `getDeductions`
- Domain: `analytics`
- Base URLs: `https://seller-analytics-api.wildberries.ru`
- Tags: Отчёты об удержаниях
- Required parameters: `dateTo`, `limit`
- Rate limit hint: Лимит запросов на один аккаунт продавца: | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 мин | 1 запрос | 1 мин | 1 запрос |
- Read-only: yes

Метод возвращает отчёт об удержаниях за [подмены и неверные вложения](https://seller.wildberries.ru/analytics-reports/dimensions-penalties/retentions) Лимит запросов на один аккаунт продавца: | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 мин | 1 запрос | 1 мин | 1 запрос |

### `GET /api/v1/analytics/antifraud-details`

- Summary: Самовыкупы
- Operation ID: `get_api-v1-analytics-antifraud-details`
- Domain: `analytics`
- Base URLs: `https://seller-analytics-api.wildberries.ru`
- Tags: Отчёты об удержаниях
- Rate limit hint: Лимит запросов на один аккаунт продавца: | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 10 мин | 1 запрос | 10 мин | 10 запросов |
- Read-only: yes

Метод возвращает отчёт об удержаниях за самовыкупы. Отчёт формируется каждую неделю по средам, до 7:00 по московскому времени, и содержит данные за одну неделю. Удержание за самовыкуп — 30% от стоимости товаров. Минимальная сумма всех удержаний — 100 000 ₽, если за неделю в ПВЗ привезли ваших товаров больше, чем на сумму 100 000 ₽. Данные доступны с августа 2023. Лимит запросов на один аккаунт продавца: | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 10 мин | 1 запрос | 10 мин | 10 запросов |

### `GET /api/v1/analytics/goods-labeling`

- Summary: Маркировка товара
- Operation ID: `get_api-v1-analytics-goods-labeling`
- Domain: `analytics`
- Base URLs: `https://seller-analytics-api.wildberries.ru`
- Tags: Отчёты об удержаниях
- Rate limit hint: Лимит запросов на один аккаунт продавца: | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 мин | 1 запрос | 1 мин | 10 запросов |
- Read-only: yes

Метод возвращает отчёт о штрафах за отсутствие обязательной маркировки товаров. В отчёте представлены фотографии товаров, на которых маркировка отсутствует либо не считывается. Можно получить данные максимум за 31 день. Данные доступны с марта 2024. Лимит запросов на один аккаунт продавца: | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 мин | 1 запрос | 1 мин | 10 запросов |

### `GET /api/v1/acceptance_report`

- Summary: Создать отчёт
- Operation ID: `get_api-v1-acceptance-report`
- Domain: `analytics`
- Base URLs: `https://seller-analytics-api.wildberries.ru`
- Tags: Платная приёмка
- Rate limit hint: Лимит запросов на один аккаунт продавца: | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 мин | 1 запрос | 1 мин | 1 запрос |
- Read-only: yes

Метод создаёт [задание на генерацию](/openapi/reports#tag/Platnaya-priyomka/paths/~1api~1v1~1acceptance_report~1tasks~1%7Btask_id%7D~1status/get) отчёта о [платной приёмке](/openapi/reports#tag/Platnaya-priyomka/paths/~1api~1v1~1acceptance_report~1tasks~1%7Btask_id%7D~1download/get). Можно получить отчёт максимум за 31 день. Лимит запросов на один аккаунт продавца: | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 мин | 1 запрос | 1 мин | 1 запрос |

### `GET /api/v1/acceptance_report/tasks/{task_id}/status`

- Summary: Проверить статус
- Operation ID: `get_api-v1-acceptance-report-tasks-task-id-status`
- Domain: `analytics`
- Base URLs: `https://seller-analytics-api.wildberries.ru`
- Tags: Платная приёмка
- Required parameters: `task_id`
- Rate limit hint: Лимит запросов на один аккаунт продавца: | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 5 сек | 1 запрос | 5 сек | 1 запрос |
- Read-only: yes

Метод возвращает статус [задания на генерацию](/openapi/reports#tag/Platnaya-priyomka/paths/~1api~1v1~1acceptance_report/get) отчёта о [платной приёмке](/openapi/reports#tag/Platnaya-priyomka/paths/~1api~1v1~1acceptance_report~1tasks~1%7Btask_id%7D~1download/get). Лимит запросов на один аккаунт продавца: | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 5 сек | 1 запрос | 5 сек | 1 запрос |

### `GET /api/v1/acceptance_report/tasks/{task_id}/download`

- Summary: Получить отчёт
- Operation ID: `get_api-v1-acceptance-report-tasks-task-id-download`
- Domain: `analytics`
- Base URLs: `https://seller-analytics-api.wildberries.ru`
- Tags: Платная приёмка
- Required parameters: `task_id`
- Rate limit hint: Лимит запросов на один аккаунт продавца: | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 мин | 1 запрос | 1 мин | 1 запрос |
- Read-only: yes

Метод возвращает отчёт о [платной приёмке](https://seller.wildberries.ru/analytics-reports/acceptance-report) по ID [задания на генерацию](/openapi/reports#tag/Platnaya-priyomka/paths/~1api~1v1~1acceptance_report/get). Лимит запросов на один аккаунт продавца: | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 мин | 1 запрос | 1 мин | 1 запрос |

### `GET /api/v1/paid_storage`

- Summary: Создать отчёт
- Operation ID: `get_api-v1-paid-storage`
- Domain: `analytics`
- Base URLs: `https://seller-analytics-api.wildberries.ru`
- Tags: Платное хранение
- Required parameters: `dateFrom`, `dateTo`
- Rate limit hint: Лимит запросов на один аккаунт продавца: | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 мин | 1 запрос | 1 мин | 5 запросов |
- Read-only: yes

Метод создаёт [задание на генерацию](/openapi/reports#tag/Platnoe-hranenie/paths/~1api~1v1~1paid_storage~1tasks~1%7Btask_id%7D~1status/get) отчёта о [платном хранении](/openapi/reports#tag/Platnoe-hranenie/paths/~1api~1v1~1paid_storage~1tasks~1%7Btask_id%7D~1download/get). Можно получить отчёт максимум за 8 дней. Лимит запросов на один аккаунт продавца: | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 мин | 1 запрос | 1 мин | 5 запросов |

### `GET /api/v1/paid_storage/tasks/{task_id}/status`

- Summary: Проверить статус
- Operation ID: `get_api-v1-paid-storage-tasks-task-id-status`
- Domain: `analytics`
- Base URLs: `https://seller-analytics-api.wildberries.ru`
- Tags: Платное хранение
- Required parameters: `task_id`
- Rate limit hint: Лимит запросов на один аккаунт продавца: | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 5 сек | 1 запрос | 5 сек | 5 запросов |
- Read-only: yes

Метод возвращает статус [задания на генерацию](/openapi/reports#tag/Platnoe-hranenie/paths/~1api~1v1~1paid_storage/get) отчёта о [платном хранении](/openapi/reports#tag/Platnoe-hranenie/paths/~1api~1v1~1paid_storage~1tasks~1%7Btask_id%7D~1download/get). Лимит запросов на один аккаунт продавца: | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 5 сек | 1 запрос | 5 сек | 5 запросов |

### `GET /api/v1/paid_storage/tasks/{task_id}/download`

- Summary: Получить отчёт
- Operation ID: `get_api-v1-paid-storage-tasks-task-id-download`
- Domain: `analytics`
- Base URLs: `https://seller-analytics-api.wildberries.ru`
- Tags: Платное хранение
- Required parameters: `task_id`
- Rate limit hint: Лимит запросов на один аккаунт продавца: | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 мин | 1 запрос | 1 мин | 1 запрос |
- Read-only: yes

Метод возвращает отчёт о [платном хранении](https://seller.wildberries.ru/analytics-reports/paid-storage/storage) по ID [задания на генерацию](/openapi/reports#tag/Platnoe-hranenie/paths/~1api~1v1~1paid_storage/get). Лимит запросов на один аккаунт продавца: | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 мин | 1 запрос | 1 мин | 1 запрос |

### `GET /api/v1/analytics/region-sale`

- Summary: Получить отчёт
- Operation ID: `get_api-v1-analytics-region-sale`
- Domain: `analytics`
- Base URLs: `https://seller-analytics-api.wildberries.ru`
- Tags: Продажи по регионам
- Rate limit hint: Лимит запросов на один аккаунт продавца: | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 10 сек | 1 запрос | 10 сек | 5 запросов |
- Read-only: yes

Метод возвращает отчёт с [данными продаж, сгруппированных по регионам стран](https://seller.wildberries.ru/analytics-reports/region-sale). Можно получить отчёт максимум за 31 день. Лимит запросов на один аккаунт продавца: | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 10 сек | 1 запрос | 10 сек | 5 запросов |

### `GET /api/v1/analytics/brand-share/brands`

- Summary: Бренды продавца
- Operation ID: `get_api-v1-analytics-brand-share-brands`
- Domain: `analytics`
- Base URLs: `https://seller-analytics-api.wildberries.ru`
- Tags: Доля бренда в продажах
- Rate limit hint: Лимит запросов на один аккаунт продавца: | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 мин | 1 запрос | 1 мин | 10 запросов |
- Read-only: yes

Метод возвращает список брендов продавца для отчёта о [доле бренда в продажах](https://seller.wildberries.ru/analytics-reports/brand-share). Можно получить только бренды, которые: - Продавались за последние 90 дней. - Есть на складе WB. Лимит запросов на один аккаунт продавца: | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 мин | 1 запрос | 1 мин | 10 запросов |

### `GET /api/v1/analytics/brand-share/parent-subjects`

- Summary: Родительские категории бренда
- Operation ID: `get_api-v1-analytics-brand-share-parent-subjects`
- Domain: `analytics`
- Base URLs: `https://seller-analytics-api.wildberries.ru`
- Tags: Доля бренда в продажах
- Required parameters: `brand`
- Rate limit hint: Лимит запросов на один аккаунт продавца: | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 5 сек | 1 запрос | 5 сек | 20 запросов |
- Read-only: yes

Метод возвращает родительские категории бренда продавца для отчёта о [доле бренда в продажах](https://seller.wildberries.ru/analytics-reports/brand-share). Можно получить отчёт максимум за 365 дней. Данные доступны с 1 ноября 2022. Лимит запросов на один аккаунт продавца: | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 5 сек | 1 запрос | 5 сек | 20 запросов |

### `GET /api/v1/analytics/brand-share`

- Summary: Получить отчёт
- Operation ID: `get_api-v1-analytics-brand-share`
- Domain: `analytics`
- Base URLs: `https://seller-analytics-api.wildberries.ru`
- Tags: Доля бренда в продажах
- Required parameters: `parentId`, `brand`
- Rate limit hint: Лимит запросов на один аккаунт продавца: | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 5 сек | 1 запрос | 5 сек | 20 запросов |
- Read-only: yes

Метод возвращает отчёт о [доле бренда продавца в продажах](https://seller.wildberries.ru/analytics-reports/brand-share). Можно получить отчёт максимум за 365 дней. Данные доступны с 1 ноября 2022. Лимит запросов на один аккаунт продавца: | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 5 сек | 1 запрос | 5 сек | 20 запросов |

### `GET /api/v1/analytics/banned-products/blocked`

- Summary: Заблокированные карточки
- Operation ID: `get_api-v1-analytics-banned-products-blocked`
- Domain: `analytics`
- Base URLs: `https://seller-analytics-api.wildberries.ru`
- Tags: Скрытые товары
- Required parameters: `sort`, `order`
- Rate limit hint: Лимит запросов на один аккаунт продавца: | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 10 сек | 1 запрос | 10 сек | 6 запросов |
- Read-only: yes

Метод возвращает список [заблокированных карточек товаров продавца](https://seller.wildberries.ru/analytics-reports/banned-products) с причинами блокировки. Лимит запросов на один аккаунт продавца: | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 10 сек | 1 запрос | 10 сек | 6 запросов |

### `GET /api/v1/analytics/banned-products/shadowed`

- Summary: Скрытые из каталога
- Operation ID: `get_api-v1-analytics-banned-products-shadowed`
- Domain: `analytics`
- Base URLs: `https://seller-analytics-api.wildberries.ru`
- Tags: Скрытые товары
- Required parameters: `sort`, `order`
- Rate limit hint: Лимит запросов на один аккаунт продавца: | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 10 сек | 1 запрос | 10 сек | 6 запросов |
- Read-only: yes

Метод возвращает список [товаров продавца, скрытых из каталога](https://seller.wildberries.ru/analytics-reports/banned-products/shadowed). Лимит запросов на один аккаунт продавца: | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 10 сек | 1 запрос | 10 сек | 6 запросов |

### `GET /api/v1/analytics/goods-return`

- Summary: Получить отчёт
- Operation ID: `get_api-v1-analytics-goods-return`
- Domain: `analytics`
- Base URLs: `https://seller-analytics-api.wildberries.ru`
- Tags: Отчёт о возвратах и перемещении товаров
- Required parameters: `dateFrom`, `dateTo`
- Rate limit hint: Лимит запросов на один аккаунт продавца: | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 мин | 1 запрос | 1 мин | 10 запросов |
- Read-only: yes

Метод возвращает отчёт о [возвратах товаров продавцу](https://seller.wildberries.ru/analytics-reports/goods-return). Можно получить отчёт максимум за 31 день. Лимит запросов на один аккаунт продавца: | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 мин | 1 запрос | 1 мин | 10 запросов |
