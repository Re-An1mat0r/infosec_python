'''Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить её на экран.'''

try:
    with open("Task5.txt", 'w') as file:
        numbers = input('Введите числа: ')
        file.write(numbers)
        numbers_new = numbers.split()
        print(sum(map(int, numbers_new)))
except ValueError:
    print('Ошибка ввода!')
