# Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

# функция
def my_func(num1, num2, num3):
    numbers = [num1, num2, num3]
    m = min(numbers)         # находим минималное число
    i = numbers.index(m)     # находим его индекс
    del numbers[i]           # удаляем по индексу
    result = sum(numbers)
    return result


# запрашиваем данные у пользователя
num1, num2, num3 = int(input()), int(input()), int(input())

# вызываем функцию
print(my_func(num1, num2, num3))