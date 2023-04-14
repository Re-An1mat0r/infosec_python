'''Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль. Проверьте его работу на данных,
вводимых пользователем. При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию
и не завершиться с ошибкой.'''


class DivisionByZeroError(Exception):
    def __init__(self, message='Деление на 0 невозможно!'):
        self.message = message
        super().__init__(self.message)


def division(a, b):
    if b == 0:
        raise DivisionByZeroError()
    return a / b


try:
    a = int(input('Введите 1-е число: '))
    b = int(input('Введите 2-е число: '))
    result = division(a, b)
    print(result)
except DivisionByZeroError as err:
    print(err)
