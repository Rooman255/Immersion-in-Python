# Решить квадратное уравнение 5x 2-10x-400 = 0 последовательно сохраняя переменные a, b, c, d, x1 и x2.


# def d(a, b, c):
#     return b ** 2 - 4 * a * c


# def x1(a, b, d):
#     return (-b + d ** 0.5) / (2 * a)


# def x2(a, b, d):
#     return (-b - d ** 0.5) / (2 * a)


# def main():
#     print()
#     print(f"Дискриминант = {d(5, -10, -400)}")
#     print(f"          X1 = {x1(5, -10, d(5, -10, -400))}")
#     print(f"          X2 = {x2(5, -10, d(5, -10, -400))}")
#     print()


# if __name__ == "__main__":
#     main()



 # *Попробуйте решить уравнения с другими значениями a, b, c.

def d(a, b, c):
    return b ** 2 - 4 * a * c


def x1(a, b, d):
    return (-b + d ** 0.5) / (2 * a)


def x2(a, b, d):
    return (-b - d ** 0.5) / (2 * a)


def main():
    print()
    print(f"Дискриминант = {d(7, -12, -600)}")
    print(f"          X1 = {x1(7, -12, d(7, -12, -600))}")
    print(f"          X2 = {x2(7, -12, d(7, -12, -600))}")
    print()


if __name__ == "__main__":
    main()
