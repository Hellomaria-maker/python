# Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры: размер
# (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
from abc import ABC, abstractmethod


class Clothers(ABC):

    @abstractmethod
    def __init__(self, name):
        self.name = name


class Coat(Clothers):
    coat_list = []

    def __init__(self, name, v):
        self.v = v
        Clothers.__init__(self, name)

    @property
    def tissue_consumption(self):
        tissue_consumption = self.v/6.5 + 0.5
        Coat.coat_list.append(tissue_consumption)
        return f'Ткань на {self.name} пальто: {tissue_consumption}'

    @staticmethod
    def all_tissue_coat():
        return sum([i for i in Coat.coat_list])


class Costume(Clothers):
    costume_list = []

    def __init__(self, name, h):
        self.h = h
        Clothers.__init__(self, name)

    @property
    def tissue_consumption(self):
        tissue_consumption = self.h * 2 + 0.3
        Costume.costume_list.append(tissue_consumption)
        return f'Ткань на {self.name} костюм: {tissue_consumption}'

    @staticmethod
    def all_tissue_costume():
        return sum([i for i in Costume.costume_list])


a = Coat("Женское", 176)
print(a.tissue_consumption)
b = Costume("Мужской", 186)
print(b.tissue_consumption)
print(f'Общий подсчет расхода ткани: {Costume.all_tissue_costume() + Coat.all_tissue_coat()}')

