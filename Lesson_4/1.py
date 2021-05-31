# Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv

def salary(hours_work, rate_hour, prize):
    person_salary = (hours_work * rate_hour) + prize
    return person_salary

hours_work, rate_hour, prize = argv

print("Заработная плата сотрудника: ", salary(hours_work, rate_hour, prize))