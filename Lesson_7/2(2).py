from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def clothing_size(self):
        pass


class Coat(Clothes):
    def __init__(self, name, parametr):
        self.name = name
        self.parametr = parametr

    @property
    def clothing_size(self):
        v = self.parametr / 6.5 + 0.5
        return v


class Costume(Clothes):
    def __init__(self, name, parametr):
        self.name = name
        self.parametr = parametr

    @property
    def clothing_size(self):
        h = self.parametr * 2 + 0.3
        return h


count_coat = int(input("Введите количество пальто: "))
coats_total_costs = 0
costume_total_costs = 0
coat_list = [Coat(input("Название пальто: "), int(input("Значение переменной H: "))) for i in range(count_coat)]
for coats in coat_list:
    print(f"На пальто {coats.name} потребуется {coats.clothing_size} метров(а) ткани")
    coats_total_costs += coats.clothing_size
print(f"На {count_coat} пальто потребуется {coats_total_costs} метров(а) ткани")

count_costume = int(input("Введите количество костюмов: "))
costume_list = [Costume(input("Название костюма: "), int(input("Значение переменной V: "))) for i in
                range(count_costume)]
for costumes in costume_list:
    print(f"На костюм {costumes.name} потребуется {costumes.clothing_size} метров(а) ткани")
    costume_total_costs += costumes.clothing_size
print(f"На {count_costume} костюмов(а) потребуется {costume_total_costs} метров(а) ткани")

total_cost = costume_total_costs + coats_total_costs
print(f"Всего потребуется {total_cost} метров ткани")