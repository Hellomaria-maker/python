# Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y.
# Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
# ПЕРВЫЙ СПОСОБ
# функция
def my_func(x, y):
    result = x ** y
    return result
# запрашиваем данные у пользователя
x, y = int(input()), int(input())
# вызываем функцию
print(my_func(x, y))

# ВТОРОЙ СПОСОБ
def my_func(x, y):
    r = 1
    y = abs(y)
    while y > 0:
       r *= x
       y -= 1
    result = 1 / r          # так как у отрцательное число
    return result
# запрашиваем данные у пользователя
x, y = int(input()), int(input())
# вызываем функцию
print(my_func(x, y))