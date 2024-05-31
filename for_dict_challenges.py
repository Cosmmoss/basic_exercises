# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]

result = {}  # создаётся словарь с парой - 'имя': кол-во повторений имени
for name in students:  # перебираем элементы (словари) списка students
    result[name['first_name']] = result.get(name['first_name'], 0) + 1  # с помощью метода get проверяем, если имя есть, то +1, если нет 0
for key, value in result.items():  # в цикле метод items() возвращает все ключи и значения словаря result
    print(key, ': ', value, sep='')
print()

# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]
name_number = {}  # создаётся словарь с парой - 'имя': кол-во повторений имени
for name in students:  # перебираем элементы (словари) из списка students
    name_number[name['first_name']] = name_number.get(name['first_name'], 0) + 1 # метод get проверяет, если имени в словаре name_number нет, то ключу присваивается знчение 0 и +1

max_num = []
for num in name_number.values():
    max_num.append(num)
max_num = max(max_num)  # определил количество повторений самого частого имени

max_name = ''
for name, num in name_number.items():  # перебираю ключ и значение словаря name_number
    if num == max_num:
        max_name = name  # определил самое частое имя

print('Самое частое имя среди учеников:', max_name)
print()

# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ],[  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]

def max_num_name(school_class):  # функция выдает самое частое имя в классе
    name_number = {}  # создаётся словарь с парой - 'имя': кол-во повторений имени
    for name in school_class:  # перебираем имена в классе
        name_number[name['first_name']] = name_number.get(name['first_name'], 0) + 1 # метод get проверяет, если имени в словаре name_number нет, то ключу присваивается знчение 0 и +1

    max_num = []
    for num in name_number.values(): 
        max_num.append(num)  # находим значение - число повторений самого частого имени
    max_num = max(max_num)  # определил самое частое имя

    max_name = ''
    for name, num in name_number.items():
        if num == max_num:
            max_name = name  # находим самое частое имя в классе

    return max_name

for num in range(len(school_students)):
    print(f'Самое частое имя в классе {num + 1}: {max_num_name(school_students[num])}')  # вызов функции для определения самого частого имени в классе
print()

# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2в', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}
for class_ in school:  # перебираем элементы списка shcool
    girls, boys= 0, 0
    for name in class_['students']:  # перебираем элементы списка students
        if is_male[name['first_name']]:  # если имя в словаре is_male соответствует True
            girls += 0
            boys += 1
        else:
            girls += 1
            boys += 0
    print(f"Класс {class_['class']}: девочки {girls}, мальчики {boys}")
print()
# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}

num_boys_in_classes = {}
num_girls_in_classes = {}
for klass in school:
    boys, girls = 0, 0
    for names in klass['students']:
        if is_male[names['first_name']]:  # если имя в словаре is_male соответствует True
            girls += 0
            boys += 1
        else:
            girls += 1
            boys += 0
    num_boys_in_classes[boys] = klass['class']  # в словарь добавляю ключ (количество мальчиков в классе): значение (класс)
    num_girls_in_classes[girls] = klass['class']  # в словарь добавляю ключ (количество девочек в классе): значение (класс)

def num_klass_with_max_students(num_students_klass):  # функция возвращает номер класса с максимальным количеством учеников
    for num, klass in num_students_klass.items():
        if num == max(num_students_klass):
            return klass
        
print('Больше всего девочек в классе', num_klass_with_max_students(num_girls_in_classes))
print('Больше всего мальчиков в классе', num_klass_with_max_students(num_boys_in_classes))

