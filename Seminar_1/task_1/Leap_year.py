
# Написать программу, которая запрашивает год и проверяет его на високосность.


def leapYear(year):

    if year % 4 != 0:

        requested_year = 'год не високосный.'

    elif year % 100 == 0:

        if year % 400 == 0:
            requested_year = 'год високосный.'
        else:
            requested_year = 'год не високосный.'

    else:
        requested_year = 'год високосный.'

    return requested_year


def main():

    year = int(input(
        '\nВведите год, обязательно учитывая год ввода Григорианского календаря с 1582 год: '))
    print(f"\n{year} - {leapYear(year)}\n")


if __name__ == "__main__":
    main()
