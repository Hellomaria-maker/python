# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц
# (зима, весна, лето, осень). Напишите решения через list и через dict.
month_number = int(input())
# Решение через dict
month_dict = {1: 'Январь', 2: 'Февраль', 3: 'Март', 4: 'Апрель', 5: 'Май', 6: 'Июнь', 7: 'Июль', 8: 'Август', 9: 'Сентябрь', 10: 'Октябрь', 11: 'Ноябрь', 12: 'Декабрь'}
month_name = month_dict.get(month_number)
print(month_name)
if month_number == 12 or month_number == 1 or month_number == 2:
    print('Зима')
elif month_number == 3 or month_number == 4 or month_number == 5:
    print('Весна')
elif month_number == 9 or month_number == 10 or month_number == 11:
    print('Осень')
else:
    print('Лето')
# Решение через list
m_name = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']
seasons = ['Зима', 'Весна', 'Лето', 'Осень']
i = month_number
print(m_name[i - 1])
if month_number == 12 or month_number == 1 or month_number == 2:
    print(seasons[0])
elif month_number == 3 or month_number == 4 or month_number == 5:
    print(seasons[1])
elif month_number == 9 or month_number == 10 or month_number == 11:
    print(seasons[3])
else:
    print(seasons[2])