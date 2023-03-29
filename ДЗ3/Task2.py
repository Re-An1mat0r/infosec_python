'''Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя: имя, фамилия,
год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
Осуществить вывод данных о пользователе одной строкой.'''


def user_data(name, surname, year, city, email, phone):
    return ' '.join([name, surname, year, city, email, phone])


print(user_data(name='Александр', surname='Петров', year='1970', city='Москва', email='apetrov@home.ru', phone='777'))
