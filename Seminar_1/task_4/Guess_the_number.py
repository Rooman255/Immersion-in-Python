from random import randint

hidden_number = randint(1, 1000)

print("\nОтгадайте число от 1 до 1000, за 10 попыток\n")

for i in range(10):

    number = int(input("\nВведите число: "))

    if number == hidden_number:
        print(f"\nВы угадали за {(i + 1)} попыток число\n")
        break
    elif number > hidden_number:
        print(
            f"\nЗагаданное число меньше, внимание осталось {10 - (i + 1)} попыток\n")

    elif number < hidden_number:
        print(
            f"\nЗагаданное число больше, внимание осталось {10 - (i + 1)} попыток\n")

print(f"Число было загадано - {hidden_number}\n")
