'''Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить, к какому времени года относится месяц (зима, весна, лето, осень). Напишите решения через list и dict.'''

seasons = {'Зима': [12, 1, 2], 'Весна': [3, 4, 5], 'Лето': [6, 7, 8], 'Осень': [9, 10, 11]}
is_finished = False
while not is_finished:
    month = int(input('Введите номер месяца: '))
    for key, value in seasons.items():
        if month in value:
            print(f'Время года: {key}')
            is_finished = True
            break
    if not is_finished:
        print('Введено неверное число. Введите число от 1 до 12')
