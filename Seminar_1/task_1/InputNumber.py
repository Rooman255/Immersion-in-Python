while True:
    multiplication = 1
    x_number = 1
    number = int(input("\nВведите число от 1 до 999: "))

    if number >= 1 and number <= 999:

        if len(str(number)) == 1:

            result = f'\nКвадрат числа {number} = {pow(number, 2)}'

        elif len(str(number)) == 2:
            x_number = number
            while number > 0:

                num = number % 10
                multiplication *= num
                number //= 10
            result = f'\nПроизведение числа {x_number} = {multiplication}'

        else:
            reversal = 0
            x_number = number
            while number != 0:
                num_rev = number % 10
                reversal = reversal * 10 + num_rev
                number //= 10
            result = f'\nЗеркальное отображение числа {x_number} = {reversal}'

    else:
        result = "\nНе входит в диапозон"

    print(result)
