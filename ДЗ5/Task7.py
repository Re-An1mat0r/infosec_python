'''Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка будет содержать данные
о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.

Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчёт средней прибыли её не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить её в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджер контекста.'''

import json

try:
    with open("Task7.txt", 'r') as f:
        content = [x.strip() for x in f.readlines() if x not in ['', '\n']]
        firms = {}

        for item in content:
            name, form, profit, loss = item.split()
            # В задании: Если фирма получила убытки, также добавить её в словарь (со значением убытков).
            # Тогда добавляем всё подряд "доходы минус расходы"
            firms[name] = float(profit) - float(loss)

        # В задании: Если фирма получила убытки, в расчёт средней прибыли её не включать.
        # Считаем средняк, только по тем кто не в минусах
        total_profit = 0
        firm_count = 0

        for firm, value in firms.items():
            if value < 0:
                continue
            total_profit += value
            firm_count += 1

        average_profit = total_profit / firm_count

        json_object = [firms, {'average_profit': average_profit}]
        json_string = json.dumps(json_object)

        with open("Task7_res.json", 'w') as r:
            r.write(json_string)
except FileNotFoundError:
    print('Файл не найден!')
