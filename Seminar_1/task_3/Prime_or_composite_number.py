while True:
    number = int(input("\nВведите число от 1 до 100000: "))

    counter = 0

    if number > 0 and number < 100001:

        for i in range(2, number // 2+1):

            if (number % i == 0):

                counter = counter+1

        if (counter <= 0):

            print(f"\nЧисло {number} является  Простым\n")

        else:

            print(f"\nЧисло {number} является Составным\n")
    else:
        print("\nВы вышли за пределы допустимого значения\n")
