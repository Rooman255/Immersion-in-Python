# Посчитайте сумму чётных элементов от 1 до n исключая кратные e.
# Используйте while

# def sum_of_even_elements_excluding(n, s, i, e):
#     while i < n:
#         i += 1
#         if i % e == 0:
#             continue
#         if i % 2 == 0:
#             s += i
#     return s


# def main():
#     print()
#     print(
#         f"Сумма чётных элементов от 1 до 901 исключая кратные 3 = {sum_of_even_elements_excluding(901, 0, 0, 3)}")
#     print()


# if __name__ == "__main__":
#     main()

# Посчитайте сумму чётных элементов от 1 до n исключая кратные e.
# Используйте for

def sum_of_even_elements_excluding(n, s, e):

    for i in range(1, n + 1):
        if i % e == 0:
            continue
        if i % 2 == 0:
            s += i
    return s


def main():
    print()
    print(
        f"Сумма чётных элементов от 1 до 505 исключая кратные 5 = {sum_of_even_elements_excluding(505, 0, 5)}")
    print()


if __name__ == "__main__":
    main()
