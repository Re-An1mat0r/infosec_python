'''Реализовать проект расчёта суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определённое название.
К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры: размер (для пальто)
и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.'''

from abc import ABC, abstractmethod


class Clothes(ABC):

    @abstractmethod
    def consumption(self):
        pass


class Coat(Clothes):
    def __init__(self, size):
        self._size = size

    @property
    def size(self):
        return self._size

    def consumption(self):
        return self.size / 6.5 + 0.5


class Suit(Clothes):
    def __init__(self, height):
        self._height = height

    @property
    def height(self):
        return self._height

    def consumption(self):
        return 2 * self.height + 0.3


coat = Coat(52)
suit = Suit(200)
print(f'Расход ткани на пальто размера {coat.size}: {coat.consumption()}')
print(f'Расход ткани на костюм для роста {suit.height}: {suit.consumption()}')
print(f'Общее колличество затраченной ткани: {coat.consumption() + suit.consumption()}')
