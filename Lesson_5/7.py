# Создать (не программно) текстовый файл, в котором каждая строка
# должна содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
# а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь
# (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
import json
profit_dict = {}
all_prof = 0
i = 0
with open('file_for_7', 'r') as file:
    for line in file:
        name, firm, earning, damage = line.split()
        profit = int(earning) - int(damage)
        if profit >= 0:
            all_prof += profit
            i += 1
            print(f'Прибыль {i} компании - {profit}')
        prof_aver = all_prof / i
    if i != 0:
        print(f'Cредняя прибыль всех компаний - {prof_aver}')
    else:
        print(f'Нет прибыльных компаний')
    profit_dict.update({'средняя прибыль': round(prof_aver)})

with open('file_7.json', 'w') as new_json:
    json.dump(profit, new_json)

    js_str = json.dumps(profit)
    print(f'Создан файл с расширением json: {js_str}')