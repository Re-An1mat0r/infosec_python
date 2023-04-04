'''Создать текстовый файл (не программно), сохранить в нём несколько строк,
выполнить подсчёт строк и слов в каждой строке.'''

try:
    with open("Task2.txt", encoding="utf-8") as file:
        my_list = file.readlines()
        print(f'Количество строк в файле {(len(my_list))}')
        for el in range(len(my_list)):
            new_list = my_list[el].split()
            print(f'В {el + 1}-ой строке {len(new_list)} слов(а)')
except FileNotFoundError:
    print('Файл не найден!')
