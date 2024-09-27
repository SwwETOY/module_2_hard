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
    print(*result, sep='')
else:
    print(print('Число не соответствует'))
