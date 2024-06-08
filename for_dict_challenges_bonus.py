"""
Пожалуйста, приступайте к этой задаче после того, как вы сделали и получили ревью ко всем остальным задачам
в этом репозитории. Она значительно сложнее.


Есть набор сообщений из чата в следующем формате:

```
messages = [
    {
        "id": "efadb781-9b04-4aad-9afe-e79faef8cffb",
        "sent_at": datetime.datetime(2022, 10, 11, 23, 11, 11, 721),
        "sent_by": 46,  # id пользователя-отправителя
        "reply_for": "7b22ae19-6c58-443e-b138-e22784878581",  # id сообщение, на которое это сообщение является ответом (может быть None)
        "seen_by": [26, 91, 71], # идентификаторы пользователей, которые видели это сообщение
        "text": "А когда ревью будет?",
    }
]
```

Так же есть функция `generate_chat_history`, которая вернёт список из большого количества таких сообщений.
Установите библиотеку lorem, чтобы она работала.

Нужно:
1. Вывести айди пользователя, который написал больше всех сообщений.
2. Вывести айди пользователя, на сообщения которого больше всего отвечали.
3. Вывести айди пользователей, сообщения которых видело больше всего уникальных пользователей.
4. Определить, когда в чате больше всего сообщений: утром (до 12 часов), днём (12-18 часов) или вечером (после 18 часов).
5. Вывести идентификаторы сообщений, который стали началом для самых длинных тредов (цепочек ответов).

Весь код стоит разбить на логические части с помощью функций.
"""
import random
import uuid
import datetime

import lorem


def generate_chat_history():
    messages_amount = random.randint(200, 1000)
    users_ids = list(
        {random.randint(1, 10000) for _ in range(random.randint(5, 20))}
    )
    sent_at = datetime.datetime.now() - datetime.timedelta(days=100)
    messages = []
    for _ in range(messages_amount):
        sent_at += datetime.timedelta(minutes=random.randint(0, 240))
        messages.append({
            "id": uuid.uuid4(),
            "sent_at": sent_at,
            "sent_by": random.choice(users_ids),
            "reply_for": random.choice(
                [
                    None,
                    (
                        random.choice([m["id"] for m in messages])
                        if messages else None
                    ),
                ],
            ),
            "seen_by": random.sample(users_ids,
                                     random.randint(1, len(users_ids))),
            "text": lorem.sentence(),
        })
    return messages

# 1. Вывести айди пользователя, который написал больше всех сообщений.
def user_wrote_most_messages(history):
    
    user_id_message = {}  # создаётся словарь с парой - 'user_id': кол-во сообщений
    for message in history:
        user_id_message[message['sent_by']] = user_id_message.get(message['sent_by'], 0) + 1

    user_id_max = max(user_id_message.items(), key=lambda items: items[1])  # определяю максимальное количество сообщений
    
    ids_with_max_messages = [] 
    for user_id, message_count in user_id_message.items():  # для определения всех айди пользователей, которые написали больше всех сообщений
        if message_count == user_id_max[1]:
            ids_with_max_messages.append(user_id)

    return f'ID пользователя(ей), который(е) написал(и) больше всех сообщений: {ids_with_max_messages}'

# 2. Вывести айди пользователя, на сообщения которого больше всего отвечали.
def user_messages_most_answered(history):

    message_db = {}
    for message in history:  # создаём словарь ключ (id message): значение (весь message)
        message_db[message['id']] = message
    
    users_counter = {}
    for message in history:  # перебираем сообщения в списке history
        if message['reply_for'] is not None:  # если id (сообщение, на которое есть ответ) не None
            parent_message = message_db[message['reply_for']]  # в правой части передаём id сообщ. message['reply_for'] по ключу id сообщ. словаря message_db. Таким образом в переменную передаётся словарь, в котором по ключу 'sent_by' id пользователя, получившего ответ на id сообщение из message['reply_for']
            user_id = parent_message['sent_by']  # в переменную user_id передаётся ID пользователя, получившего ответ
            users_counter[user_id] = users_counter.get(user_id, 0) + 1  # создаётся словарь ключ (ID пользователя): значение (количество сообщений)
    
    user_id_max = max(users_counter.items(), key=lambda items: items[1])  # определяется кортеж (ID пользователя, максимальное количество сообщений)
    
    users_id_max = [] 
    for key, value in users_counter.items():  # для определения всех айди пользователей (в случае повторений максимального количества сообщений)
        if value == user_id_max[1]:
            users_id_max.append(key)

    return f'ID пользователя(ей), на сообщения которого(ых) больше всего отвечали: {users_id_max}' 

# 3. Вывести айди пользователей, сообщения которых видело больше всего уникальных пользователей.
def id_users_posts_seen_most_uniq_users(history):
    
    id_user_uniq_users = {}  # создаём словарь - ключ (id_message): значение (количество уникальных пользователей)
    for message in history:
        id_user_uniq_users[message['id']] = len(message['seen_by']) # по ключу id_message передаем количество уникальных пользователей
    
    num_max_uniq_users = max(id_user_uniq_users.items(), key=lambda items: items[1])  # определяется кортеж (id_messege, максимальное количество уникальных пользователей)
  
    users_id_max = []  # создаём список, чтобы элементы были типа int; будут повторяться одинаковые id_user 
    for message in history:
        if len(message['seen_by']) == num_max_uniq_users[1]:  # если кол-во уник. сообщ. равно максимальному кол-ву
            users_id_max.append(message['sent_by'])  # в список добавить ID пользователя

    return f'ID пользователей, сообщения которых видело больше всего уникальных пользователей: {users_id_max}'

# 4. Определить, когда в чате больше всего сообщений: утром (до 12 часов), днём (12-18 часов) или вечером (после 18 часов).

def time_most_messages_in_chat(history):

    num_all_messages = {                  # словарь - ключ (период времени): значение (id сообщений за это время). 
            'утром (до 12 часов)': [],
            'днём (12-18 часов)': [],
            'вечером (после 18 часов)': []
            }
  
    for message in history:
        if 0 <= message['sent_at'].hour < 12:  # если время сообщения больше заданного
            num_all_messages['утром (до 12 часов)'].append(message['id'])  # добавить 'id' message в список словаря num_all_message
        elif 12 <= message['sent_at'].hour < 18:
            num_all_messages['днём (12-18 часов)'].append(message['id'])
        elif 18 <= message['sent_at'].hour < 24:
            num_all_messages['вечером (после 18 часов)'].append(message['id'])
    
    time_max_messages = (max(num_all_messages.items(), key=lambda items: len(items[1])))  # определяем в какой период времени больше всего сообщений

    return f"В чате больше всего сообщений: {time_max_messages[0]}"

# 5. Вывести идентификаторы сообщений, который стали началом для самых длинных тредов (цепочек ответов).

def get_threads_length(history):
    messages_db = {}
    for message in history:
        messages_db[message.get('id')] = message

    count = {}  # ключ (№ id сообщения): значение (длина цепочки)

    def get_thread_length(message_id):
        if message_id is None:
            return 0
        message = messages_db[message_id]
        parent_id = message['reply_for']
        thread_len = get_thread_length(parent_id) + 1
        return thread_len

    for message in history:
        count[message['id']] = get_thread_length(message['id'])

    max_thread_length = max(count.items(), key=lambda items: items[1])

    all_max_thread_length = []  # id сообщений, которые стали началом для самых длинных цепочек ответов
    for id, length in count.items():
        if length == max_thread_length[1]:  
            all_max_thread_length.append(id)  # в список добавить ID сообщения

    return f"Идентификаторы сообщений, которые стали началом для самых длинных тредов (цепочек ответов): {all_max_thread_length}" 

if __name__ == "__main__":
    history = generate_chat_history()
    print(user_wrote_most_messages(history))
    print(user_messages_most_answered(history))
    print(id_users_posts_seen_most_uniq_users(history))
    print(time_most_messages_in_chat(history))
    print(get_threads_length(history))