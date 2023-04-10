'''Реализуйте базовый класс Car.
у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Вызовите методы и покажите результат.'''


class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} поехала'

    def stop(self):
        return f'{self.name} остановилась'

    def turn(self, direction):
        return f'{self.name} повернула на{direction}'

    def show_speed(self):
        return f'{self.name}: текущая скорость {self.speed}км/ч'


class TownCar(Car):

    def show_speed(self):
        max_speed = 60
        if self.speed > max_speed:
            return f'{self.name}: текущая скорость {self.speed}км/ч, превышаете разшённую скорость на {self.speed - max_speed}км/ч'
        return f'{self.name}: текущая скорость {self.speed}км/ч'


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        max_speed = 40
        if self.speed > max_speed:
            return f'{self.name}: текущая скорость {self.speed}км/ч, превышаете разшённую скорость на {self.speed - max_speed}км/ч'
        return f'{self.name}: текущая скорость {self.speed}км/ч'


class PoliceCar(Car):
    pass


town_car = TownCar(90, 'Красный', 'Mazda', False)
sport_car = SportCar(150, 'Чёрный', 'Ferrari', False)
work_car = WorkCar(80, 'Баклажан', 'Лада', False)
police_car = PoliceCar(100, 'Белый', 'BMW', True)
print(town_car.go())
print(town_car.show_speed())
print(town_car.turn('право'))
print(town_car.stop())
print(sport_car.go())
print(sport_car.show_speed())
print(work_car.go())
print(work_car.show_speed())
print(work_car.turn('лево'))
print(police_car.go())
print(police_car.show_speed())
