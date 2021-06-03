# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.
staff_list = ['Gorshkova 100000\n', 'Ivanov 50000\n', 'Sergeev 15000\n', 'Demidov 200000\n', 'Popov 8000\n']
# внесем данные о сотрудниках в файл
with open("Staff", 'w') as file:
    file.writelines(staff_list)

with open('Staff', 'r') as my_staff:
    line_counter = 0
    for _ in my_staff:            # посчитаем количество строк чтобы узнать сколько всего сотруднико в компании
        line_counter += 1
        all_income = 0
    my_staff.seek(0)
    print(f'{line_counter} всего сотрудников в компании')
    for _ in range(line_counter):
        line = my_staff.readline()
        one_person_inform = line.split(' ')          # разделим строку по пробелу чтобы отделить фамилию от зп
        all_income += int(one_person_inform[1])      # суммируем зп всех сотрудников
        if int(one_person_inform[1]) <= 20000:       # находим у кого зп < 20000
            print(f'{one_person_inform[0]} зарабатывает меньше 20 т.р')
    average_income = all_income/line_counter         # находим среднюю величину дохода
print(f'{average_income} средняя величины дохода сотрудников')