# Общее

- Source YAML: `01-general.yaml`
- Version: `general`
- Methods: `7`
- Domains: common

## Summary

В этом разделе: - [общая информация о WB API](/openapi/api-information#tag/Vvedenie) - как [начать работу с WB API](/openapi/api-information#tag/Vvedenie/Kak-nachat-rabotu-s-API) - как [авторизоваться](/openapi/api-information#tag/Avtorizaciya) и [создавать токены](/openapi/api-information#tag/Avtorizaciya/Kak-sozdat-personalnyj-bazovyj-ili-testovyj-token) - основные [статус-коды ответов](/openapi/api-information#tag/Vvedenie/Status-kody-HTTP) - [лимиты запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) - как обратиться в [поддержку](/openapi/api-information#tag/Vvedenie/Podderzhka) С помощью методов этого раздела вы можете: - проверить [подключение к WB API](/openapi/api-information#tag/Proverka-podklyucheniya-k-WB-API/paths/~1ping/get) - получить [новости портала продавцов](/openapi/api-information#tag/API-novostej/paths/~1api~1communications~1v2~1news/get) - получить [информацию о продавце](/openapi/api-information#tag/Informaciya-o-prodavce/paths/~1api~1v1~1seller-info/get) - [управлять пользователями продавца](/openapi/api-information#tag/Upravlenie-polzovatelyami-prodavca)

## Tags

- Введение
- Авторизация
- Проверка подключения к WB API
- API новостей
- Информация о продавце
- Управление пользователями продавца

## Methods

### `GET /ping`

- Summary: Проверка подключения
- Operation ID: `get_ping`
- Domain: `common`
- Base URLs: `https://common-api.wildberries.ru`
- Tags: Проверка подключения к WB API
- Rate limit hint: Лимит действует отдельно для каждого варианта метода в зависимости от домена
- Read-only: yes

Метод проверяет: 1. Успешно ли запрос доходит до WB API 2. Валидность токена авторизации и URL запроса 3. Совпадают ли категория токена и сервис Метод не предназначен для проверки доступности сервисов WB У каждого сервиса есть свой вариант метода в зависимости от домена: | Категория | URL запроса | |---------------|-----------------------| | Контент | `https://content-api.wildberries.ru/ping` `https://content-api-sandbox.wildberries.ru/ping` | | Аналитика | `https://seller-analytics-api.wildberries.ru/ping` | | Цены и скидки | `https://discounts-prices-api.wildberries.ru/ping` `https://discounts-prices-api-sandbox.wildberries.ru/ping` | | Маркетплейс | `https://marketplace-api.wildberries.ru/ping` | | Статистика | `https://statistics-api.wildberries.ru/ping` `https://statistics-api-sandbox.wildberries.ru/ping` | | Продвижение | `https://advert-api.wildberries.ru/ping` `https://advert-api-sandbox.wildberries.ru/ping` | | Вопросы и отзывы | `https://feedbacks-api.wildberries.ru/ping` `https://feedbacks-api-sandbox.wildberries.ru/ping` | | Чат с покупателями | `https://buyer-chat-api.wildberries.ru/ping` | | Поставки | `https://supplies-api.wildberries.ru/ping` | | Возвраты покупателями | `https://returns-api.wildberries.ru/ping` | | Документы | `https://documents-api.wildberries.ru/ping` | | Финансы | `https://finance-api.wildberries.ru/ping` | | Тарифы, Новости, Информация о продавце | `https://common-api.wildberries.ru/ping` | | Управление пользователями продавца | `https://user-management-api.wildberries.ru/ping` | Максимум 3 запроса за 30 секунд . Если попытаться автоматизировать использование метода, запросы будут временно заблокированы. Лимит действует отдельно для каждого варианта метода в зависимости от домена

### `GET /api/communications/v2/news`

- Summary: Получение новостей портала продавцов
- Operation ID: `get_api-communications-v2-news`
- Domain: `common`
- Base URLs: `https://common-api.wildberries.ru`
- Tags: API новостей
- Rate limit hint: Лимит запросов на один аккаунт продавца: | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 мин | 1 запрос | 1 мин | 10 запросов |
- Read-only: yes

Метод позволяет получать новости портала продавцов. Для получения успешного ответа необходимо указать один из параметров `from` или `fromID`. За один запрос можно получить не более 100 новостей. Лимит запросов на один аккаунт продавца: | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 мин | 1 запрос | 1 мин | 10 запросов |

### `GET /api/v1/seller-info`

- Summary: Получение информации о продавце
- Operation ID: `get_api-v1-seller-info`
- Domain: `common`
- Base URLs: `https://common-api.wildberries.ru`
- Tags: Информация о продавце
- Rate limit hint: Лимит запросов на один аккаунт продавца: | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 мин | 1 запрос | 1 мин | 10 запросов |
- Read-only: yes

Метод позволяет получать наименование продавца и ID его профиля. В запросе можно использовать любой токен, у которого не выбрана опция **Тестовый контур**. Лимит запросов на один аккаунт продавца: | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 мин | 1 запрос | 1 мин | 10 запросов |

### `POST /api/v1/invite`

- Summary: Создать приглашение для нового пользователя
- Operation ID: `post_api-v1-invite`
- Domain: `common`
- Base URLs: `https://user-management-api.wildberries.ru`
- Tags: Управление пользователями продавца
- Rate limit hint: Лимит запросов на один аккаунт продавца: | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 сек | 1 запрос | 1 сек | 5 запросов |

Метод доступен по Персональному токену Метод создаёт приглашение для нового пользователя с настройкой доступов к разделам профиля продавца. Как выдаются права доступа: - Если `access` пустой (`[]`) или не указан — по умолчанию выдаются все доступы, кроме доступов к витрине (`showcase`) и **Джем** (`changeJam`) - Если в `access` указана часть разделов профиля, то кроме тех доступов, что указаны в запросе, также выдаются все доступы по умолчанию - Если в `access` перечислены все возможные разделы, доступы будут выданы согласно запросу, без доступов по умолчанию - Если в `access` дважды указан один и тот же раздел (`code`): - при разных значениях `disabled` (`true` и `false`) доступ не будет выдан - при одинаковых значениях `"disabled": true` доступ не будет выдан - при одинаковых значениях `"disabled": false` доступ будет выдан Лимит запросов на один аккаунт продавца: | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 сек | 1 запрос | 1 сек | 5 запросов |

### `GET /api/v1/users`

- Summary: Получить список активных или приглашённых пользователей продавца
- Operation ID: `get_api-v1-users`
- Domain: `common`
- Base URLs: `https://user-management-api.wildberries.ru`
- Tags: Управление пользователями продавца
- Rate limit hint: Лимит запросов на один аккаунт продавца: | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 сек | 1 запрос | 1 сек | 5 запросов |
- Read-only: yes

Метод доступен по Персональному токену Метод возвращает список активных или приглашённых пользователей профиля продавца. Чтобы выбрать список, укажите значение параметра `isInviteOnly`: - `isInviteOnly=true` — список приглашённых пользователей, которые ещё не активировали доступ - `isInviteOnly=false` или не указан — список активных пользователей По каждому пользователю можно получить: - роль пользователя - разделы, к которым есть доступы - статус приглашения Список приглашённых пользователей в ответе всегда отсортирован по дате создания: от новых до старых. Лимит запросов на один аккаунт продавца: | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 сек | 1 запрос | 1 сек | 5 запросов |

### `PUT /api/v1/users/access`

- Summary: Изменить права доступа пользователей
- Operation ID: `put_api-v1-users-access`
- Domain: `common`
- Base URLs: `https://user-management-api.wildberries.ru`
- Tags: Управление пользователями продавца
- Rate limit hint: Лимит запросов на один аккаунт продавца: | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 сек | 1 запрос | 1 сек | 5 запросов |

Метод доступен по Персональному токену Метод меняет права доступа одному или нескольким пользователям. Обновляются только права доступа, переданные в параметрах запроса. Остальные поля остаются без изменений. Лимит запросов на один аккаунт продавца: | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 сек | 1 запрос | 1 сек | 5 запросов |

### `DELETE /api/v1/user`

- Summary: Удалить пользователя
- Operation ID: `delete_api-v1-user`
- Domain: `common`
- Base URLs: `https://user-management-api.wildberries.ru`
- Tags: Управление пользователями продавца
- Required parameters: `deletedUserID`
- Rate limit hint: Лимит запросов на один аккаунт продавца: | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 сек | 1 запрос | 1 сек | 10 запросов |

Метод доступен по Персональному токену Метод удаляет пользователя из [списка сотрудников продавца](/openapi/api-information#tag/Upravlenie-polzovatelyami-prodavca/paths/~1api~1v1~1users/get). Этому пользователю будет закрыт доступ в профиль продавца. Лимит запросов на один аккаунт продавца: | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 сек | 1 запрос | 1 сек | 10 запросов |
