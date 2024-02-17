
import numpy as np


class Matrix:

    # операция для инициализации объектов
    def __init__(self, matrix: list[list]):

        self.value = matrix

        self.length = len(matrix)

        self.height = len(matrix[0])

    def value(self):

        return self._value

    def value(self, matrix: list[list]):
        self._value = matrix


# операция определения строкового представления объекта


    def __str__(self):

        return "\n".join(str(i) for i in self.value)


# операция определения поведения оператора равенства (==)


    def __eq__(self, other):

        if isinstance(other, Matrix):

            if self.height == other.height and self.length == other.length:

                result = []

                for i in range(self.length):

                    for j in range(self.height):

                        result.append(self.value[i][j] == other.value[i][j])

                return all(result)

        return False


# операции сравнения


    def __lt__(self, other):

        if isinstance(other, Matrix):

            if self.height == other.height and self.length == other.length:

                result = []

                for i in range(self.length):

                    for j in range(self.height):

                        result.append(self.value[i][j] < other.value[i][j])

                return all(result)

        return False


# операции сложения


    def __add__(self, other):

        if isinstance(other, Matrix):

            if self.height == other.height and self.length == other.length:

                result = [[] for i in range(self.length)]

                for i in range(self.length):

                    for j in range(self.height):

                        result[i].append(self.value[i][j] + other.value[i][j])

                return Matrix(result)


#  операции умножения;


    def __mul__(self, other):

        if isinstance(other, Matrix):

            if self.height == other.length:

                result = [[sum(a * b for a, b in zip(self_row, other_col))

                           for other_col in zip(*other.value)]

                          for self_row in self.value]

            elif self.length == other.height:

                result = [[sum(a * b for a, b in zip(self_col, other_row))

                           for self_col in zip(*self.value)]

                          for other_row in other.value]

            return Matrix(result)

        return False


if __name__ == '__main__':

    matrix_1 = Matrix(np.random.randint(0, 20, (3, 3)))
    matrix_2 = Matrix(np.random.randint(0, 20, (3, 3)))
    matrix_3 = Matrix(np.random.randint(0, 20, (3, 3)))

    print(f"\nМатрица №1\n{matrix_1}\n")
    print(f"\nМатрица №2\n{matrix_2}\n")
    print(f"\nМатрица №3\n{matrix_3}\n")
    print("Сравнение матриц:\n")
    print(f"Матрица №1 == Матрица №2 - {matrix_1 == matrix_2}\n")
    print(f"Матрица №1 == Матрица №3 - {matrix_1 == matrix_3}\n")
    print(f"Матрица №1 < Матрица №2 - {matrix_1 < matrix_2}\n")
    print(f"Матрица №1 > Матрица №2 - {matrix_1 > matrix_2}\n")
    print(f"Матрица №1 < Матрица №3 - {matrix_1 < matrix_3}\n")
    print(f"Матрица №1 > Матрица №3 - {matrix_1 > matrix_3}\n")

    matrix_add = matrix_1 + matrix_2

    print(f"Матрица №1 + Матрица №2 = \n{matrix_add}\n")

    matrix_mult = matrix_2 * matrix_3

    print(f"Матрица №2 * Матрица №3 = \n{matrix_mult}\n")
