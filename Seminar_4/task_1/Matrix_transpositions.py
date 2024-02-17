def transpositionsMatrix():
    matrix = [[8, 5, 1], [7, 9, 6], [8, 5, 4], [2, 7, 6]]

    print(f"\nМатрица до транспортировки:\n")
    for i in matrix:
        print(i)

    matrix_transpositions = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix_transpositions[j][i] = matrix[i][j]

    print(f"\nМатрица после транспортировки:\n")
    for i in matrix_transpositions:
        print(i)


def main():
    transpositionsMatrix()


if __name__ == '__main__':
    main()
