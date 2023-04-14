'''1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц: 3 на 2, 3 на 3, 2 на 4.

31    32         3    5    32        3    5    8    3
37    43         2    4    6         8    3    7    1
51    86        -1   64   -8
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно —
первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.'''


class Matrix:
    def __init__(self, matrix_list):
        self.matrix_list = matrix_list

    def __str__(self):
        return '\n'.join(map(str, self.matrix_list))

    def __add__(self, other):
        if len(self.matrix_list) != len(other.matrix_list):
            raise ValueError("Матрицы должны быть одинакового размера")
        for el in range(len(self.matrix_list)):
            if len(self.matrix_list[el]) != len(other.matrix_list[el]):
                raise ValueError("Матрицы должны быть одинакового размера")
            for el_2 in range(len(other.matrix_list[el])):
                self.matrix_list[el][el_2] = self.matrix_list[el][el_2] + other.matrix_list[el][el_2]
        return Matrix.__str__(self)


matrix = Matrix([[3, 5, 32], [2, -4, 6], [1, 32, 8], [2, -1, 3]])
new_matrix = Matrix([[5, 0, -5], [3, 0, 3], [-5, 3, 2], [4, 2, 7]])
m = matrix + new_matrix
print(m)
