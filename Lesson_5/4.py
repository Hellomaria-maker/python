# Создать (не программно) текстовый файл со следующим содержимым: One — 1, Two — 2, Three — 3, Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл
my_vocab = {'One': 'odin', 'Two': 'dva', 'Three': 'tri', 'Four': 'chetyte'}
result = []
with open('file_for_4', 'r') as my_file:
    for _ in range(4):
        line = my_file.readline()
        my_str = line.split(" - ")
        if my_str[0] in my_vocab:
            word = my_vocab[my_str[0]]
            result.append(word + ' - ' + my_str[1])
    print(result)

with open('new_file_for_4.txt', 'w') as new_file:
    new_file.writelines(result)
