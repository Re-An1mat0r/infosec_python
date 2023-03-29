'''Реализовать функцию my_func(), которая принимает три позиционных аргумента
и возвращает сумму наибольших двух аргументов.'''


def my_func(a, b, c):
    arr = [a, b, c]
    arr.sort(reverse=True)
    return arr[0] + arr[1]


print(my_func(100, 500, 300))
