# Представлен список чисел. Необходимо вывести элементы исходного списка,
# значения которых больше предыдущего элемента. [12, 44, 4, 10, 78, 123]

def big_elem(all_elem):  # функция для формирования списка с помощью генератора
    elements_filter = [all_elem[i + 1] for i in range(len(all_elem) - 1) if all_elem[i + 1] > all_elem[i]]
    return elements_filter
# задаем исходный список
all_elem = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

print(big_elem(all_elem))


