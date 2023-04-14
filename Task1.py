''' Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod. Он должен извлекать число,
месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod,
должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.'''


class Date:
    def __init__(self, date_str):
        self.date_str = date_str

    @classmethod
    def date_extract(cls, date_str):
        day, month, year = map(int, date_str.split('-'))
        return day, month, year

    @staticmethod
    def validate_date(date_str):
        day, month, year = Date.date_extract(date_str)
        if day < 1 or day > 31:
            return False
        if month < 1 or month > 12:
            return False
        if year < 0 or year > 10000:
            return False
        return True


if Date.validate_date('13-04-2023'):
    print('Дата указана верно')
else:
    print('Дата указана неверно')
