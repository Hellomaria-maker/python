# Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.
num = int(input())
max_digit = 0                  # пусть в начале максимальная цифра = 0
while num != 0:                # пока в числе не закончатся цифры мы будем брать последнюю
    last_digit = num % 10
    if last_digit > max_digit:  # сравнивать последнюю с максимальной
        max_digit = last_digit
    num = num // 10             # перед началом нового цикла отбрасывать последнюю цифру
print(max_digit)