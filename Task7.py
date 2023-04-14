'''Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число».
Реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта.
Для этого создаёте экземпляры класса (комплексные числа), выполните сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.'''


class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return ComplexNumber(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        return ComplexNumber(self.a*other.a - self.b*other.b,
                             self.a*other.b + self.b*other.a)

    def __str__(self):
        return f"{self.a} + {self.b}i"


num1 = ComplexNumber(1, 2)
num2 = ComplexNumber(3, 5)
sum_num = num1 + num2
product_num = num1 * num2
print(f'Сумма комплексных чисел равна: {sum_num}')
print(f'Произведение комплексных чисел равно: {product_num}')
