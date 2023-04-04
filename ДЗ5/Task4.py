'''Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Напишите программу, открывающую файл на чтение и считывающую построчно данные. При этом английские числительные
должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.'''

numbers = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_text = []
try:
    with open("Task4.txt", encoding="utf-8") as file:
        with open("Task4_new.txt", 'r+', encoding="utf-8") as new_file:
            lines = file.readlines()
            for i in lines:
                key, value = i.split(' — ')
                new_text.append(f'{numbers[key]} — {value}')
            new_file.writelines(new_text)
except FileNotFoundError:
    print('Файл не найден!')
