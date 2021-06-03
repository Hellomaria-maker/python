# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

with open('file_for_2', 'r') as my_text:
    line_counter = 0
    word_counter = 0
    symbol_counter = 0
    for _ in my_text:
        line_counter += 1
    my_text.seek(0)
    print(f'{line_counter} строки в файле')
    for i in range(line_counter):
        line = my_text.readline()
        word_counter += line.count(' ') + 1
        print(f'{word_counter}  слов в {i + 1} строке')
        word_counter = 0





