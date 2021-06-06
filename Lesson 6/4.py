# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar)
# и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
# выведите результат. Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        if self.is_police is False:
            print(f'В нашем городе новый автомобиль: {self.color} {self.name}')
        else:
            print(f'В нашем городе новый автомобиль: {self.color} {self.name}. Это полицейская машина!')

    def stop(self):
        return f"Машина {self.name} остановилась"

    def go(self):
        return f"Машина {self.name} поехала"

    def turn(self, direction):
        self.direction = direction
        return f"Машина {self.name} повернула в {self.direction}"

    def show_speed(self):
        return f'В настоящее время у автомобиля {self.name} скорость: {self.speed}'


class TownCar(Car):
    def show_speed(self):
        if self.speed <= 40:
            return f'В настоящее время у автомобиля {self.name} скорость: {self.speed}. '\
                   f'Это нормальная скорость для такого автомбомиля!'
        else:
            return f'В настоящее время у автомобиля {self.name} скорость: {self.speed}. '\
                   f'Это слишком высокая скорость для такого автомбомиля!'


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed <= 60:
            return f'В настоящее время у автомобиля {self.name} скорость: {self.speed}. ' \
                   f'Это нормальная скорость для такого автомбомиля!'
        else:
            return f'В настоящее время у автомобиля {self.name} скорость: {self.speed}. ' \
                   f'Это слишком высокая скорость для такого автомбомиля!'


class PoliceCar(Car):
    pass


new_town_car = TownCar(80, 'синий', 'BMW', False)
print(new_town_car.show_speed())
print(new_town_car.turn('лево'))
print(new_town_car.stop())

new_police_car = PoliceCar(60, 'белый', 'Lada', True)
print(new_police_car.show_speed())

new_work_car = WorkCar(30, 'черный', 'Porsche', False)
print(new_work_car.show_speed())
print(new_work_car.turn('право'))
print(new_work_car.stop())

