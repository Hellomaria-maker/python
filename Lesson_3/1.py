# Реализовать функцию, принимающую два числа (позиционные аргументы)
# и выполняющую их деление. Числа запрашивать у пользователя,
# предусмотреть обработку ситуации деления на ноль

# функция
def number_division (num1, num2):
    if num2 == 0:
        result = "Деление на 0 запрещено"
        return result
    else:
        result = num1 / num2
        return result

# запрашиваем данные у пользователя
num1, num2 = int(input()), int(input())

# вызываем функцию
print(number_division(num1, num2))