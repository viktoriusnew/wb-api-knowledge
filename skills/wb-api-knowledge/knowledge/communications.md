# Общение с покупателями

- Source YAML: `09-communications.yaml`
- Version: `communication`
- Methods: `25`
- Domains: communications, returns

## Summary

Узнать больше об общении с покупателями можно в справочном центре С помощью методов общения с покупателями вы можете работать с: 1. [Вопросами](/openapi/user-communication#tag/Voprosy) и [отзывами](/openapi/user-communication#tag/Otzyvy) покупателей 2. [Закреплёнными отзывами](/openapi/user-communication#tag/Zakreplyonnye-otzyvy) 3. [Чатами с покупателями](/openapi/user-communication#tag/Chat-s-pokupatelyami) 4. [Заявками покупателей на возврат](/openapi/user-communication#tag/Vozvraty-pokupatelyami) Узнать, как использовать методы в бизнес-кейсах, можно в инструкции по работе с разделом Общение с покупателями

## Tags

- Вопросы
- Отзывы
- Закреплённые отзывы
- Чат с покупателями
- Возвраты покупателями

## Methods

### `GET /api/v1/new-feedbacks-questions`

- Summary: Непросмотренные отзывы и вопросы
- Operation ID: `get_api-v1-new-feedbacks-questions`
- Domain: `communications`
- Base URLs: `https://feedbacks-api.wildberries.ru`
- Tags: Вопросы
- Rate limit hint: Лимит запросов на один аккаунт продавца для всех методов категории Вопросы и отзывы : | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 сек | 3 запроса | 333 мс | 6 запросов |
- Read-only: yes

Метод проверяет наличие непросмотренных [вопросов](/openapi/user-communication#tag/Voprosy/paths/~1api~1v1~1questions/get) и [отзывов](/openapi/user-communication#tag/Otzyvy/paths/~1api~1v1~1feedbacks/get) от покупателей. Если у продавца есть непросмотренные вопросы или отзывы, возвращает `true`. Лимит запросов на один аккаунт продавца для всех методов категории Вопросы и отзывы : | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 сек | 3 запроса | 333 мс | 6 запросов |

### `GET /api/v1/questions/count-unanswered`

- Summary: Неотвеченные вопросы
- Operation ID: `get_api-v1-questions-count-unanswered`
- Domain: `communications`
- Base URLs: `https://feedbacks-api.wildberries.ru`
- Tags: Вопросы
- Rate limit hint: Лимит запросов на один аккаунт продавца для всех методов категории Вопросы и отзывы : | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 сек | 3 запроса | 333 мс | 6 запросов |
- Read-only: yes

Метод возвращает общее количество неотвеченных [вопросов](/openapi/user-communication#tag/Voprosy/paths/~1api~1v1~1questions/get) и количество неотвеченных вопросов за сегодня. Лимит запросов на один аккаунт продавца для всех методов категории Вопросы и отзывы : | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 сек | 3 запроса | 333 мс | 6 запросов |

### `GET /api/v1/questions/count`

- Summary: Количество вопросов
- Operation ID: `get_api-v1-questions-count`
- Domain: `communications`
- Base URLs: `https://feedbacks-api.wildberries.ru`
- Tags: Вопросы
- Rate limit hint: Лимит запросов на один аккаунт продавца для всех методов категории Вопросы и отзывы : | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 сек | 3 запроса | 333 мс | 6 запросов |
- Read-only: yes

Метод возвращает количество отвеченных или неотвеченных [вопросов](/openapi/user-communication#tag/Voprosy/paths/~1api~1v1~1questions/get) за заданный период. Лимит запросов на один аккаунт продавца для всех методов категории Вопросы и отзывы : | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 сек | 3 запроса | 333 мс | 6 запросов |

### `GET /api/v1/questions`

- Summary: Список вопросов
- Operation ID: `get_api-v1-questions`
- Domain: `communications`
- Base URLs: `https://feedbacks-api.wildberries.ru`
- Tags: Вопросы
- Required parameters: `isAnswered`, `take`, `skip`
- Rate limit hint: Лимит запросов на один аккаунт продавца для всех методов категории Вопросы и отзывы : | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 сек | 3 запроса | 333 мс | 6 запросов |
- Read-only: yes

Метод возвращает список вопросов по заданным фильтрам. Вы можете: - получить данные отвеченных и неотвеченных вопросов - сортировать вопросы по дате - настроить пагинацию и количество вопросов в ответе Можно получить максимум 10 000 вопросов в одном ответе Лимит запросов на один аккаунт продавца для всех методов категории Вопросы и отзывы : | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 сек | 3 запроса | 333 мс | 6 запросов |

### `PATCH /api/v1/questions`

- Summary: Работа с вопросами
- Operation ID: `patch_api-v1-questions`
- Domain: `communications`
- Base URLs: `https://feedbacks-api.wildberries.ru`
- Tags: Вопросы
- Rate limit hint: Лимит запросов на один аккаунт продавца для всех методов категории Вопросы и отзывы : | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 сек | 3 запроса | 333 мс | 6 запросов |

В зависимости от тела запроса, метод позволяет: - отметить [вопрос](/openapi/user-communication#tag/Voprosy/paths/~1api~1v1~1questions/get) как просмотренный - отклонить вопрос - ответить на вопрос или отредактировать ответ Отредактировать ответ на вопрос можно 1 раз в течение 60 дней после отправки ответа Лимит запросов на один аккаунт продавца для всех методов категории Вопросы и отзывы : | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 сек | 3 запроса | 333 мс | 6 запросов |

### `GET /api/v1/question`

- Summary: Получить вопрос по ID
- Operation ID: `get_api-v1-question`
- Domain: `communications`
- Base URLs: `https://feedbacks-api.wildberries.ru`
- Tags: Вопросы
- Required parameters: `id`
- Rate limit hint: Лимит запросов на один аккаунт продавца для всех методов категории Вопросы и отзывы : | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 сек | 3 запроса | 333 мс | 6 запросов |
- Read-only: yes

Метод возвращает данные [вопроса](/openapi/user-communication#tag/Voprosy/paths/~1api~1v1~1questions/get) по его ID. Далее вы можете [работать с этим вопросом](/openapi/user-communication#tag/Voprosy/paths/~1api~1v1~1questions/patch). Лимит запросов на один аккаунт продавца для всех методов категории Вопросы и отзывы : | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 сек | 3 запроса | 333 мс | 6 запросов |

### `GET /api/v1/feedbacks/count-unanswered`

- Summary: Необработанные отзывы
- Operation ID: `get_api-v1-feedbacks-count-unanswered`
- Domain: `communications`
- Base URLs: `https://feedbacks-api.wildberries.ru`
- Tags: Отзывы
- Rate limit hint: Лимит запросов на один аккаунт продавца для всех методов категории Вопросы и отзывы : | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 сек | 3 запроса | 333 мс | 6 запросов |
- Read-only: yes

Метод возвращает: - количество необработанных [отзывов](/openapi/user-communication#tag/Otzyvy/paths/~1api~1v1~1feedbacks/get) за сегодня и за всё время Лимит запросов на один аккаунт продавца для всех методов категории Вопросы и отзывы : | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 сек | 3 запроса | 333 мс | 6 запросов |

### `GET /api/v1/feedbacks/count`

- Summary: Количество отзывов
- Operation ID: `get_api-v1-feedbacks-count`
- Domain: `communications`
- Base URLs: `https://feedbacks-api.wildberries.ru`
- Tags: Отзывы
- Rate limit hint: Лимит запросов на один аккаунт продавца для всех методов категории Вопросы и отзывы : | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 сек | 3 запроса | 333 мс | 6 запросов |
- Read-only: yes

Метод возвращает количество обработанных или необработанных [отзывов](/openapi/user-communication#tag/Otzyvy/paths/~1api~1v1~1feedbacks/get) за заданный период. Лимит запросов на один аккаунт продавца для всех методов категории Вопросы и отзывы : | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 сек | 3 запроса | 333 мс | 6 запросов |

### `GET /api/v1/feedbacks`

- Summary: Список отзывов
- Operation ID: `get_api-v1-feedbacks`
- Domain: `communications`
- Base URLs: `https://feedbacks-api.wildberries.ru`
- Tags: Отзывы
- Required parameters: `isAnswered`, `take`, `skip`
- Rate limit hint: Лимит запросов на один аккаунт продавца для всех методов категории Вопросы и отзывы : | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 сек | 3 запроса | 333 мс | 6 запросов |
- Read-only: yes

Метод возвращает список отзывов по заданным фильтрам. Вы можете: - получить данные обработанных и необработанных отзывов - сортировать отзывы по дате - настроить пагинацию и количество отзывов в ответе Лимит запросов на один аккаунт продавца для всех методов категории Вопросы и отзывы : | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 сек | 3 запроса | 333 мс | 6 запросов |

### `POST /api/v1/feedbacks/answer`

- Summary: Ответить на отзыв
- Operation ID: `post_api-v1-feedbacks-answer`
- Domain: `communications`
- Base URLs: `https://feedbacks-api.wildberries.ru`
- Tags: Отзывы
- Rate limit hint: Лимит запросов на один аккаунт продавца для всех методов категории Вопросы и отзывы : | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 сек | 3 запроса | 333 мс | 6 запросов |

Метод позволяет ответить на [отзыв](/openapi/user-communication#tag/Otzyvy/paths/~1api~1v1~1feedbacks/get) покупателя. ID отзыва не валидируется. Если в запросе вы передали некорректный ID, вы не получите ошибку. Лимит запросов на один аккаунт продавца для всех методов категории Вопросы и отзывы : | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 сек | 3 запроса | 333 мс | 6 запросов |

### `PATCH /api/v1/feedbacks/answer`

- Summary: Отредактировать ответ на отзыв
- Operation ID: `patch_api-v1-feedbacks-answer`
- Domain: `communications`
- Base URLs: `https://feedbacks-api.wildberries.ru`
- Tags: Отзывы
- Rate limit hint: Лимит запросов на один аккаунт продавца для всех методов категории Вопросы и отзывы : | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 сек | 3 запроса | 333 мс | 6 запросов |

Метод позволяет отредактировать уже отправленный [ответ на отзыв](/openapi/user-communication#tag/Otzyvy/paths/~1api~1v1~1feedbacks~1answer/post) покупателя. Отредактировать ответ можно только один раз в течение 60 дней c момента отправки. ID отзыва не валидируется. Если в запросе вы передали некорректный ID, вы не получите ошибку. Лимит запросов на один аккаунт продавца для всех методов категории Вопросы и отзывы : | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 сек | 3 запроса | 333 мс | 6 запросов |

### `POST /api/v1/feedbacks/order/return`

- Summary: Возврат товара по ID отзыва
- Operation ID: `post_api-v1-feedbacks-order-return`
- Domain: `communications`
- Base URLs: `https://feedbacks-api.wildberries.ru`
- Tags: Отзывы
- Rate limit hint: Лимит запросов на один аккаунт продавца для всех методов категории Вопросы и отзывы : | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 сек | 3 запроса | 333 мс | 6 запросов |

Метод запрашивает возврат товара, по которому оставлен [отзыв](/openapi/user-communication#tag/Otzyvy/paths/~1api~1v1~1feedbacks/get). Возврат доступен для отзывов с полем `"isAbleReturnProductOrders": true`. Лимит запросов на один аккаунт продавца для всех методов категории Вопросы и отзывы : | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 сек | 3 запроса | 333 мс | 6 запросов |

### `GET /api/v1/feedback`

- Summary: Получить отзыв по ID
- Operation ID: `get_api-v1-feedback`
- Domain: `communications`
- Base URLs: `https://feedbacks-api.wildberries.ru`
- Tags: Отзывы
- Required parameters: `id`
- Rate limit hint: Лимит запросов на один аккаунт продавца для всех методов категории Вопросы и отзывы : | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 сек | 3 запроса | 333 мс | 6 запросов |
- Read-only: yes

Метод возвращает данные [отзыва](/openapi/user-communication#tag/Otzyvy/paths/~1api~1v1~1feedbacks/get) по его ID. Лимит запросов на один аккаунт продавца для всех методов категории Вопросы и отзывы : | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 сек | 3 запроса | 333 мс | 6 запросов |

### `GET /api/v1/feedbacks/archive`

- Summary: Список архивных отзывов
- Operation ID: `get_api-v1-feedbacks-archive`
- Domain: `communications`
- Base URLs: `https://feedbacks-api.wildberries.ru`
- Tags: Отзывы
- Required parameters: `take`, `skip`
- Rate limit hint: Лимит запросов на один аккаунт продавца для всех методов категории Вопросы и отзывы : | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 сек | 3 запроса | 333 мс | 6 запросов |
- Read-only: yes

Метод возвращает список архивных [отзывов](/openapi/user-communication#tag/Otzyvy/paths/~1api~1v1~1feedbacks/get). Отзыв становится архивным, если: - на отзыв получен ответ - на отзыв не получен ответ в течение 30 дней - в отзыве нет текста и фото Лимит запросов на один аккаунт продавца для всех методов категории Вопросы и отзывы : | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 сек | 3 запроса | 333 мс | 6 запросов |

### `GET /api/feedbacks/v1/pins`

- Summary: Список закреплённых и откреплённых отзывов
- Operation ID: `get_api-feedbacks-v1-pins`
- Domain: `communications`
- Base URLs: `https://feedbacks-api.wildberries.ru`
- Tags: Закреплённые отзывы
- Rate limit hint: Лимит запросов на один аккаунт продавца для всех методов категории Вопросы и отзывы : | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 сек | 3 запроса | 333 мс | 6 запросов |
- Read-only: yes

Метод предоставляет список закреплённых и откреплённых отзывов. Откреплёнными считаются только отзывы, которые были откреплены автоматически по причинам, указанным в ответе в поле `unpinnedCause`. Лимит запросов на один аккаунт продавца для всех методов категории Вопросы и отзывы : | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 сек | 3 запроса | 333 мс | 6 запросов |

### `POST /api/feedbacks/v1/pins`

- Summary: Закрепить отзывы
- Operation ID: `post_api-feedbacks-v1-pins`
- Domain: `communications`
- Base URLs: `https://feedbacks-api.wildberries.ru`
- Tags: Закреплённые отзывы
- Rate limit hint: Лимит запросов на один аккаунт продавца для всех методов категории Вопросы и отзывы : | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 сек | 3 запроса | 333 мс | 6 запросов |

Метод позволяет закрепить отзывы в карточке товара или в группе [объединённых](https://dev.wildberries.ru/news/101#obuedinenie-i-razuedinenie-kartochek-tovarov) карточек. Чтобы получить ID отзывов, используйте метод [Список закреплённых и откреплённых отзывов](/openapi/user-communication#tag/Zakreplyonnye-otzyvy/paths/~1api~1feedbacks~1v1~1pins/get). Метод доступен по [подписке Джем](https://seller.wildberries.ru/monetization/jam) или c [тарифной опцией](https://seller.wildberries.ru/tariff-constructor) **Закрепление отзыва**. Лимит запросов на один аккаунт продавца для всех методов категории Вопросы и отзывы : | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 сек | 3 запроса | 333 мс | 6 запросов |

### `DELETE /api/feedbacks/v1/pins`

- Summary: Открепить отзывы
- Operation ID: `delete_api-feedbacks-v1-pins`
- Domain: `communications`
- Base URLs: `https://feedbacks-api.wildberries.ru`
- Tags: Закреплённые отзывы
- Rate limit hint: Лимит запросов на один аккаунт продавца для всех методов категории Вопросы и отзывы : | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 сек | 3 запроса | 333 мс | 6 запросов |

Метод позволяет открепить отзывы в карточке товара или в группе [объединённых](https://dev.wildberries.ru/news/101#obuedinenie-i-razuedinenie-kartochek-tovarov) карточек. Чтобы получить `pinId` — ID операций закрепления, используйте метод [Список закреплённых и откреплённых отзывов](/openapi/user-communication#tag/Zakreplyonnye-otzyvy/paths/~1api~1feedbacks~1v1~1pins/get). Лимит запросов на один аккаунт продавца для всех методов категории Вопросы и отзывы : | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 сек | 3 запроса | 333 мс | 6 запросов |

### `GET /api/feedbacks/v1/pins/count`

- Summary: Количество закреплённых и откреплённых отзывов
- Operation ID: `get_api-feedbacks-v1-pins-count`
- Domain: `communications`
- Base URLs: `https://feedbacks-api.wildberries.ru`
- Tags: Закреплённые отзывы
- Rate limit hint: Лимит запросов на один аккаунт продавца для всех методов категории Вопросы и отзывы : | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 сек | 3 запроса | 333 мс | 6 запросов |
- Read-only: yes

Метод возвращает количество закреплённых и откреплённых отзывов за заданный период. Лимит запросов на один аккаунт продавца для всех методов категории Вопросы и отзывы : | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 сек | 3 запроса | 333 мс | 6 запросов |

### `GET /api/feedbacks/v1/pins/limits`

- Summary: Лимиты закреплённых отзывов
- Operation ID: `get_api-feedbacks-v1-pins-limits`
- Domain: `communications`
- Base URLs: `https://feedbacks-api.wildberries.ru`
- Tags: Закреплённые отзывы
- Rate limit hint: лимиты закреплённых отзывов по тарифу и подписке.
- Read-only: yes

Метод возвращает лимиты закреплённых отзывов по тарифу и подписке. Лимит запросов на один аккаунт продавца для всех методов категории Вопросы и отзывы : | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 сек | 3 запроса | 333 мс | 6 запросов |

### `GET /api/v1/seller/chats`

- Summary: Список чатов
- Operation ID: `get_api-v1-seller-chats`
- Domain: `communications`
- Base URLs: `https://buyer-chat-api.wildberries.ru`
- Tags: Чат с покупателями
- Rate limit hint: Лимит запросов на один аккаунт продавца: | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 10 сек | 10 запросов | 1 сек | 10 запросов |
- Read-only: yes

Метод возвращает список всех чатов продавца. По этим данным можно получить [события чатов](/openapi/user-communication#tag/Chat-s-pokupatelyami/paths/~1api~1v1~1seller~1events/get) или [отправить сообщение покупателю](/openapi/user-communication#tag/Chat-s-pokupatelyami/paths/~1api~1v1~1seller~1message/post). Лимит запросов на один аккаунт продавца: | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 10 сек | 10 запросов | 1 сек | 10 запросов |

### `GET /api/v1/seller/events`

- Summary: События чатов
- Operation ID: `get_api-v1-seller-events`
- Domain: `communications`
- Base URLs: `https://buyer-chat-api.wildberries.ru`
- Tags: Чат с покупателями
- Rate limit hint: Лимит запросов на один аккаунт продавца: | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 10 сек | 10 запросов | 1 сек | 10 запросов |
- Read-only: yes

Метод возвращает список событий всех [чатов с покупателями](/openapi/user-communication#tag/Chat-s-pokupatelyami/paths/~1api~1v1~1seller~1chats/get). Чтобы получить все события: 1. Сделайте первый запрос без параметра `next`. 2. Повторяйте запрос со значением параметра `next` из ответа на предыдущий запрос, пока `totalEvents` не станет равным `0`. Это будет означать, что вы получили все события. Лимит запросов на один аккаунт продавца: | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 10 сек | 10 запросов | 1 сек | 10 запросов |

### `POST /api/v1/seller/message`

- Summary: Отправить сообщение
- Operation ID: `post_api-v1-seller-message`
- Domain: `communications`
- Base URLs: `https://buyer-chat-api.wildberries.ru`
- Tags: Чат с покупателями
- Rate limit hint: Лимит запросов на один аккаунт продавца: | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 10 сек | 10 запросов | 1 сек | 10 запросов |

Метод отправляет сообщения в [чат с покупателем](/openapi/user-communication#tag/Chat-s-pokupatelyami/paths/~1api~1v1~1seller~1chats/get). Лимит запросов на один аккаунт продавца: | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 10 сек | 10 запросов | 1 сек | 10 запросов |

### `GET /api/v1/seller/download/{id}`

- Summary: Получить файл из сообщения
- Operation ID: `get_api-v1-seller-download-id`
- Domain: `communications`
- Base URLs: `https://buyer-chat-api.wildberries.ru`
- Tags: Чат с покупателями
- Required parameters: `id`
- Rate limit hint: Лимит запросов на один аккаунт продавца: | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 10 сек | 10 запросов | 1 сек | 10 запросов |
- Read-only: yes

Метод возвращает файл или изображение из сообщения по его ID. Лимит запросов на один аккаунт продавца: | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 10 сек | 10 запросов | 1 сек | 10 запросов |

### `GET /api/v1/claims`

- Summary: Заявки покупателей на возврат
- Operation ID: `get_api-v1-claims`
- Domain: `returns`
- Base URLs: `https://returns-api.wildberries.ru`
- Tags: Возвраты покупателями
- Rate limit hint: Лимит запросов на один аккаунт продавца: | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 мин | 20 запросов | 3 сек | 10 запросов |
- Read-only: yes

Метод возвращает заявки покупателей на возврат товаров за последние 14 дней. Вы можете [отвечать на эти заявки](/openapi/user-communication#tag/Vozvraty-pokupatelyami/paths/~1api~1v1~1claim/patch). Лимит запросов на один аккаунт продавца: | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 мин | 20 запросов | 3 сек | 10 запросов |

### `PATCH /api/v1/claim`

- Summary: Ответ на заявку покупателя
- Operation ID: `patch_api-v1-claim`
- Domain: `returns`
- Base URLs: `https://returns-api.wildberries.ru`
- Tags: Возвраты покупателями
- Rate limit hint: Лимит запросов на один аккаунт продавца: | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 мин | 20 запросов | 3 сек | 10 запросов |

Метод отправляет ответ на [заявку](/openapi/user-communication#tag/Vozvraty-pokupatelyami/paths/~1api~1v1~1claims/get) покупателя на возврат товаров. Лимит запросов на один аккаунт продавца: | Период | Лимит | Интервал | Всплеск | | --- | --- | --- | --- | | 1 мин | 20 запросов | 3 сек | 10 запросов |
