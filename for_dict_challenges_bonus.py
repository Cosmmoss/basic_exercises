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
    for user_id in history:
        user_id_message[user_id['sent_by']] = user_id_message.get(user_id['sent_by'], 0) + 1

    user_id_max = max(user_id_message.items(), key=lambda items: items[1])  # определяю максимальное количество сообщений
    
    users_id_max = [] 
    for key, value in user_id_message.items():  # для определения всех айди пользователей, которые написали больше всех сообщений
        if value >= user_id_max[1]:
            users_id_max.append(key)

    return f'ID пользователя(ей), который(е) написал(и) больше всех сообщений: {users_id_max}'

# 2. Вывести айди пользователя, на сообщения которого больше всего отвечали.
def user_messages_most_answered(history):

    message_db = {}
    for message in history:  # создаём словарь ключ (id message): значение (весь message)
        message_db[message['id']] = message
    users_counter = {}
    for message in message_db.values():  # перебираем значения, созданного выше словаря message_db
        if message['reply_for'] is not None:  # если ответ на сообщение пользователя не None
            parent_message = message  # в переменную parent_message передаётся весь message
            user_id = parent_message['sent_by']  # в переменную user_id передаётся ID пользователя
            users_counter[user_id] = users_counter.get(user_id, 0) + 1  # создаётся словарь ключ (ID пользователя): значение (количество сообщений, направленных ему)
    
    user_id_max = max(users_counter.items(), key=lambda items: items[1])  # определяется кортеж (ID пользователя, максимальное количество сообщений)
    
    users_id_max = [] 
    for key, value in users_counter.items():  # для определения всех айди пользователей (в случае повторений максимального количества сообщений), на сообщения которого больше всего отвечали
        if value == user_id_max[1]:
            users_id_max.append(key)

    return f'ID пользователя(ей), на сообщения которого(ых) больше всего отвечали: {users_id_max}'

# 3. Вывести айди пользователей, сообщения которых видело больше всего уникальных пользователей.
def id_users_posts_seen_most_uniq_users(history):
    messages_db = {}
    for message in history:
        messages_db[message['id']] = message
    
    id_user_uniq_users = {}  # создаём словарь ключ (id_messege): значение (количество уникальных пользователей)
    for mess in messages_db.values():
        id_user_uniq_users[mess['id']] = mess['seen_by'] = len(mess['seen_by']) # замена значения по ключу seen_by в словаре messages_db
    
    num_max_uniq_user = max(id_user_uniq_users.items(), key=lambda items: items[1])  # определяется кортеж (id_messege, максимальное количество уникальных пользователей)

    # users_id_max = {}  можно создать словарь и подсчитать максимальное количество уникальных просмотров с учётом повторяющихся id_user
    users_id_max = set()  # создаём множество, чтобы не дублировались одинаковые id_user
    for message in messages_db.values():
        if message['seen_by'] == num_max_uniq_user[1]:
            # users_id_max[message['sent_by']] = users_id_max.get(message['sent_by'], 0) + 1
            users_id_max.add(message['sent_by'])
      
    return f'ID пользователей, сообщения которых видело больше всего уникальных пользователей: {users_id_max}'

# 4. Определить, когда в чате больше всего сообщений: утром (до 12 часов), днём (12-18 часов) или вечером (после 18 часов).

def time_most_messages_in_chat(history):
    # Период времени с 00:00:00 по 05:59:59 не учитывается в соответствии с заданием

    num_all_messages = {                  # словарь - ключ (период времени): значение (id сообщений за это время). 
            'утром (до 12 часов)': [],
            'днём (12-18 часов)': [],
            'вечером (после 18 часов)': []
            }

    for message in history:
        if '06:00:00' <= message['sent_at'].strftime('%H:%M:%S') <= '12:00:00':  # если время сообщения больше заданного
            num_all_messages['утром (до 12 часов)'].append(message['id'])  # добавить в список словаря num_all_message
        elif '12:00:01' <= message['sent_at'].strftime('%H:%M:%S') <= '18:00:00':
            num_all_messages['днём (12-18 часов)'].append(message['id'])
        elif '18:00:01' <= message['sent_at'].strftime('%H:%M:%S') <= '23:59:59':
            num_all_messages['вечером (после 18 часов)'].append(message['id'])

    time_max_messages = (max(num_all_messages.items(), key=lambda items: len(items[1])))  # определяем в какой период времени больше всего сообщений

    return f"В чате больше всего сообщений: {time_max_messages[0]}"


if __name__ == "__main__":
    history = generate_chat_history()
    print(user_wrote_most_messages(history))
    print(user_messages_most_answered(history))
    print(id_users_posts_seen_most_uniq_users(history))
    print(time_most_messages_in_chat(history))