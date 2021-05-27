# Реализовать функцию, принимающую несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения,
# город проживания, email, телефон. Функция должна
# принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.

# функция
def person_date (name, surname, year, city, email, ph_number):
    person = []
    person.append(name), person.append(surname), person.append(year)
    person.append(city), person.append(email), person.append(ph_number)
    return person

# запрашиваем данные у пользователя
name, surname, year, city, email, ph_number = input(), input(), input(), input(), input(), input()

# вызываем функцию
print('Данные пользователя:', *person_date(name, surname, year, city, email, ph_number), end='')
print()
print('Данные пользователя:', *person_date(name = 'Мария', surname= 'Горшкова', year = '1997', city = 'Spb', email = '@', ph_number = 8), end='')