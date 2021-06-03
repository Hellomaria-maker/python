# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.
my_text = []

while True:
    s = input()
    if s == '':          # свидетельство окончания ввода данных
        break
    else:
        s += '\n'
        my_text.append(s)
        with open('my_file.txt', 'w') as my_file:
            my_file.writelines(my_text)








