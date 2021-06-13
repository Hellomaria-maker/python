# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию
# и не завершиться с ошибкой.

class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


dividend = input("Введите делимое: ")
denominator = input("Введите делитель: ")

try:
    denominator = int(denominator)
    dividend = int(dividend)
    if denominator == 0:
        raise OwnError("На ноль делить нельзя!")
except OwnError as err:
    print(err)
else:
    quotient = dividend/denominator
    print(f"Результат деления: {quotient}")