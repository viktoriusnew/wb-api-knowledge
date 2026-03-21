# Тарифы

- Source YAML: `10-tariffs.yaml`
- Version: `tariffs`
- Methods: `5`
- Domains: common

## Summary

Узнать больше о комиссиях и тарифах можно в справочном центре В разделе описаны методы получения: 1. [Комиссий](/openapi/wb-tariffs#tag/Komissii) 2. [Тарифов на остаток](/openapi/wb-tariffs#tag/Tarify-na-ostatok) 3. [Тарифов на возврат товаров продавцу](/openapi/wb-tariffs#tag/Stoimost-vozvrata-prodavcu)

## Tags

- Комиссии
- Тарифы на остаток
- Тарифы на поставку
- Стоимость возврата продавцу

## Methods

### `GET /api/v1/tariffs/commission`

- Summary: Комиссия по категориям товаров
- Operation ID: `get_api-v1-tariffs-commission`
- Domain: `common`
- Base URLs: `https://common-api.wildberries.ru`
- Tags: Комиссии
- Rate limit hint: Лимит запросов на один аккаунт продавца: | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 мин | 1 запрос | 1 мин | 2 запроса |
- Read-only: yes

Метод возвращает данные о [комиссии](https://seller.wildberries.ru/dynamic-product-categories/commission) WB по [родительским категориям товаров](/openapi/work-with-products#tag/Kategorii-predmety-i-harakteristiki/paths/~1content~1v2~1object~1parent~1all/get) согласно модели продаж. Лимит запросов на один аккаунт продавца: | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 мин | 1 запрос | 1 мин | 2 запроса |

### `GET /api/v1/tariffs/box`

- Summary: Тарифы для коробов
- Operation ID: `get_api-v1-tariffs-box`
- Domain: `common`
- Base URLs: `https://common-api.wildberries.ru`
- Tags: Тарифы на остаток
- Rate limit hint: Лимит запросов на один аккаунт продавца: | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 мин | 60 запросов | 1 сек | 5 запросов |
- Read-only: yes

Для товаров, которые поставляются на склад в коробах, метод возвращает [тарифы на остаток](https://seller.wildberries.ru/dynamic-product-categories): - доставка со склада или пункта приёма до покупателя - доставка от покупателя до пункта приёма - хранение на складе WB Лимит запросов на один аккаунт продавца: | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 мин | 60 запросов | 1 сек | 5 запросов |

### `GET /api/v1/tariffs/pallet`

- Summary: Тарифы для монопаллет
- Operation ID: `get_api-v1-tariffs-pallet`
- Domain: `common`
- Base URLs: `https://common-api.wildberries.ru`
- Tags: Тарифы на остаток
- Rate limit hint: Лимит запросов на один аккаунт продавца: | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 мин | 60 запросов | 1 сек | 5 запросов |
- Read-only: yes

Для товаров, которые поставляются на склад WB на монопаллетах, метод возвращает [стоимость](https://seller.wildberries.ru/dynamic-product-categories): - доставки со склада до покупателя - доставки от покупателя до склада - хранения на складе WB Лимит запросов на один аккаунт продавца: | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 мин | 60 запросов | 1 сек | 5 запросов |

### `GET /api/tariffs/v1/acceptance/coefficients`

- Summary: Тарифы на поставку
- Operation ID: `get_api-tariffs-v1-acceptance-coefficients`
- Domain: `common`
- Base URLs: `https://common-api.wildberries.ru`
- Tags: Тарифы на поставку
- Rate limit hint: Лимит запросов на один аккаунт продавца: | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 мин | 6 запросов | 10 сек | 6 запросов |
- Read-only: yes

Метод возвращает тарифы на поставку для конкретных складов на ближайшие 14 дней. Приёмка для поставки доступна только при сочетании: coefficient — 0 или 1 и allowUnload — true Лимит запросов на один аккаунт продавца: | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 мин | 6 запросов | 10 сек | 6 запросов |

### `GET /api/v1/tariffs/return`

- Summary: Тарифы на возврат
- Operation ID: `get_api-v1-tariffs-return`
- Domain: `common`
- Base URLs: `https://common-api.wildberries.ru`
- Tags: Стоимость возврата продавцу
- Rate limit hint: Лимит запросов на один аккаунт продавца: | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 мин | 60 запросов | 1 сек | 5 запросов |
- Read-only: yes

Метод возвращает [тарифы](https://seller.wildberries.ru/dynamic-product-categories/return-cost): - на перевозку товаров со склада WB или из пункта приёма до продавца - на обратную перевозку возвратов, которые не забрал продавец Лимит запросов на один аккаунт продавца: | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 мин | 60 запросов | 1 сек | 5 запросов |
