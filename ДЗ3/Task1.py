'''Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.'''


def numb(arg1, arg2):
    try:
        div = float(arg1) / float(arg2)
    except (ZeroDivisionError, ValueError) as error:
        return f'Ошибка! {error}'
    return div


a = input('Укажите 1-е число: ')
b = input('Укажите 2-е число: ')
print(numb(a, b))
