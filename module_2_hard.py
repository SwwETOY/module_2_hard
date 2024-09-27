
# def get_password(n):
#     # Функция get_password(n) создает пустой список pairs для хранения подходящих пар чисел.
#     pairs = []
#     # print (f"pairs = {pairs} n = {n}")
#     # Перебирает все возможные пары чисел от 1 до 20 с помощью вложенных циклов for.
#     for i in range(1, 21):
#         for j in range(i + 1, 21):
#              print(f"i = {i} j = {j} n = {n}")
#             # Проверяет, делится ли n на сумму текущей пары (i+j)(i+j) без остатка.
#             if n % (i + j) == 0:
#                  print (f" {n} % ({i} + {j}) == 0")
#                 # Если условие выполняется, добавляет пару в список pairs.
#                 pairs.append(f"{i}{j}")
#                 # print (f"Добавляет пару чисел {i}{j} в список pairs.")
#                 # print (f"Список с добавленной парой чисел: \npairs = {pairs}")
#
#     # После проверки всех пар объединяет их в одну строку и возвращает как результат.
#     # print (f".join({pairs})")
#     result = ''.join(pairs)
#     # print (f"result = {result}")
#     return result

##############################################
def code(n):
    result = []  # создаём пустой список
    for i in range(1, n + 1):  #
        for j in range(i + 1, n + 1):  #
            sum_ = i + j  # сумма
            if n % sum_ == 0:  # Полученное число n делим на сумму i и j без остатка
                result.append(i)  # добовляем полученый результат в список
                result.append(j)  # добовляем полученый результат в список
    return result  # возврощаем результат


n = int(input('Число на левом камне от 3 до 20:'))  #
if n >= 3 and n <= 20:
    result = code(n)
    # print(print('Число не соответствует'))
# print(*result, sep='')  # выводим результат в консоль без пробелов
    print(*result, sep='')
else:
    print(print('Число не соответствует'))
#################################################

# def code(n):
#     key = ''
#     for a in  n_list:
#         for b in n_list[n_list.index(a) + 1:]:
#             c = a + b
#             if n % c == 0:
#                 key += f'{a}{b}'
#     return key
#
# n_list = list(range(1, 21))
# n = int(input('Введите значение ребуса от 3 до 20:'))
# if 3 >= n <= 20:
#     result = code(n)
#     print(result)
# else:
#     print('Введите значение в диапозоне от 3 до 20')