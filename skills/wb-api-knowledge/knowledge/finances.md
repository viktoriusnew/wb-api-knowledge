# Документы и бухгалтерия

- Source YAML: `13-finances.yaml`
- Version: `finances`
- Methods: `6`
- Domains: documents, finance, statistics

## Summary

Узнать больше о документах и бухгалтерии можно в справочном центре Просмотр [баланса](/openapi/financial-reports-and-accounting#tag/Balans), [финансовых отчётов](/openapi/financial-reports-and-accounting#tag/Finansovye-otchyoty) и [документов](/openapi/financial-reports-and-accounting#tag/Dokumenty) продавца.

## Tags

- Баланс
- Финансовые отчёты
- Документы

## Methods

### `GET /api/v1/account/balance`

- Summary: Получить баланс продавца
- Operation ID: `get_api-v1-account-balance`
- Domain: `finance`
- Base URLs: `https://finance-api.wildberries.ru`
- Tags: Баланс
- Rate limit hint: Лимит запросов на один аккаунт продавца: | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 мин | 1 запрос | 1 мин | 1 запрос |
- Read-only: yes

Метод возвращает данные виджета баланса на [главной странице](https://seller.wildberries.ru) портала продавцов. Лимит запросов на один аккаунт продавца: | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 мин | 1 запрос | 1 мин | 1 запрос |

### `GET /api/v5/supplier/reportDetailByPeriod`

- Summary: Отчёт о продажах по реализации
- Operation ID: `get_api-v5-supplier-reportdetailbyperiod`
- Domain: `statistics`
- Base URLs: `https://statistics-api.wildberries.ru`
- Tags: Финансовые отчёты
- Required parameters: `dateFrom`, `dateTo`
- Rate limit hint: Лимит запросов на один аккаунт продавца: | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 минута | 1 запрос | 1 минута | 1 запрос |
- Read-only: yes

Метод возвращает детализации к [отчётам реализации](https://seller.wildberries.ru/suppliers-mutual-settlements). Данные доступны с 29 января 2024 года. Вы можете выгрузить данные в Google Таблицы Лимит запросов на один аккаунт продавца: | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 минута | 1 запрос | 1 минута | 1 запрос |

### `GET /api/v1/documents/categories`

- Summary: Категории документов
- Operation ID: `get_api-v1-documents-categories`
- Domain: `documents`
- Base URLs: `https://documents-api.wildberries.ru`
- Tags: Документы
- Rate limit hint: Лимит запросов на один аккаунт продавца: | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 10 сек | 1 запрос | 10 сек | 5 запросов |
- Read-only: yes

Метод возвращает категории документов для получения [списка документов продавца](/openapi/financial-reports-and-accounting#tag/Dokumenty/paths/~1api~1v1~1documents~1list/get). Лимит запросов на один аккаунт продавца: | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 10 сек | 1 запрос | 10 сек | 5 запросов |

### `GET /api/v1/documents/list`

- Summary: Список документов
- Operation ID: `get_api-v1-documents-list`
- Domain: `documents`
- Base URLs: `https://documents-api.wildberries.ru`
- Tags: Документы
- Rate limit hint: Лимит запросов на один аккаунт продавца: | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 10 сек | 1 запрос | 10 сек | 5 запросов |
- Read-only: yes

Метод возвращает список документов продавца. Вы можете получить [один](/openapi/financial-reports-and-accounting#tag/Dokumenty/paths/~1api~1v1~1documents~1download/get) или [несколько](/openapi/financial-reports-and-accounting#tag/Dokumenty/paths/~1api~1v1~1documents~1download~1all/post) документов из полученного списка. Лимит запросов на один аккаунт продавца: | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 10 сек | 1 запрос | 10 сек | 5 запросов |

### `GET /api/v1/documents/download`

- Summary: Получить документ
- Operation ID: `get_api-v1-documents-download`
- Domain: `documents`
- Base URLs: `https://documents-api.wildberries.ru`
- Tags: Документы
- Required parameters: `serviceName`, `extension`
- Rate limit hint: Лимит запросов на один аккаунт продавца: | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 10 сек | 1 запрос | 10 сек | 5 запросов |
- Read-only: yes

Метод загружает один документ из [списка документов продавца](/openapi/financial-reports-and-accounting#tag/Dokumenty/paths/~1api~1v1~1documents~1list/get). Лимит запросов на один аккаунт продавца: | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 10 сек | 1 запрос | 10 сек | 5 запросов |

### `POST /api/v1/documents/download/all`

- Summary: Получить документы
- Operation ID: `post_api-v1-documents-download-all`
- Domain: `documents`
- Base URLs: `https://documents-api.wildberries.ru`
- Tags: Документы
- Rate limit hint: Лимит запросов на один аккаунт продавца: | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 5 мин | 1 запрос | 5 мин | 5 запросов |
- Read-only: yes

Метод загружает несколько документов из [списка документов продавца](/openapi/financial-reports-and-accounting#tag/Dokumenty/paths/~1api~1v1~1documents~1list/get). Лимит запросов на один аккаунт продавца: | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 5 мин | 1 запрос | 5 мин | 5 запросов |
