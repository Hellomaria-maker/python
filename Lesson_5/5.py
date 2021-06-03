# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран. 4 45 6 7 89 667 543 2 123 876 98 45 34
num_sum = 0
with open('file_for_5.txt', 'w+') as file_for_5:
    file_for_5.writelines('1 2 3')
    file_for_5.seek(0)

with open('file_for_5.txt', 'r') as file_for_sum:
    for _ in file_for_sum:
        line = file_for_sum.readline()
        line_list = line.split(' ')
        for i in range(len(line_list)):
            num_sum += int(line_list[i])
print(f'{num_sum} сумма чисел из файла')

