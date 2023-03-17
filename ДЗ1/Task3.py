"""Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369."""

n = int(input('Введите число: '))
nn = str(n) + str(n)
nnn = str(n) + str(n) + str(n)
result = n + int(nn) + int(nnn)
print(f'Сумма чисел {n} + {nn} + {nnn} равна: {result}')
