import random
from test_1 import solve

# Возьмем для примера 10 случайных событий.
for _ in range(10):
    # Формируется список из случайных чисел.
    # Множество берется для исключения повторяющихся значений.
    # Затем множество преобразуется в список.
    my_list = list(set(random.randint(1, 100) for _ in range(10)))
    # Берется два случайных индекса из списка.
    a, b = random.randint(0, len(my_list) - 1), random.randint(0, len(my_list) - 1)
    # Вычисляется target на основании двух случайных индексов.
    target = my_list[a] + my_list[b]

    print(f'Список чисел: {my_list}.')
    print(f'Случайный индекс 1: {a}, Случайный индекс 2: {b}.')
    print(f'{my_list[a]} + {my_list[b]} = {target}.')
    # Функция ищет два индекса, подходящие по условию задачи.
    # Индексы из функции могут не совпадать с индексами, взятыми выше с помощью случайных чисел.
    # Так как подходящая сумма может быть найдена и под другими индексами из списка.
    print(f'Найденные с помощью функции индексы: {solve(my_list, target)}.')
    print('-' * 50)
