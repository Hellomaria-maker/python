# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
# «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod,
# должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.
class Date:

    def __init__(self, date):
        self.date = date

    def __str__(self):
        return f"Введена дата {self.date}"

    @classmethod
    def date_extract(cls, date):
        date_list = date.split('-')
        day = int(date_list[0])
        month = int(date_list[1])
        year = int(date_list[2])
        return f"День: {day} \nМесяц: {month} \nГод: {year}"

    @staticmethod
    def date_validator(date):
        date_list = date.split('-')
        day = int(date_list[0])
        month = int(date_list[1])
        year = int(date_list[2])
        if 0 < day <= 31 and 1 <= month <= 12 and 1990 <= year:
             print("Дата задана верно!")
        else:
             print("Дата задана неверно!")


a = Date("26-9-1997")
print(a)
print(Date.date_extract("26-9-1997"))
print(Date.date_validator("26-9-1997"))

