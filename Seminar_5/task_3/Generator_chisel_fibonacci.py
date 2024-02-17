import random


def fibonacci_generator(max):
    a, b = 0, 1
    while a < max:
        yield a
        a, b = b, a + b


list_of_generated_numbers = []

numbers = list(range(1, 101))
random.shuffle(numbers)
numbers_generated = int(
    input("Введите количество рандомно генерируемых чисел: "))

for i in range(numbers_generated):
    for n in fibonacci_generator(numbers[i]+1):
        list_of_generated_numbers.append(n)
    print(f"Последовательность {numbers[i]} - {list_of_generated_numbers}")
    list_of_generated_numbers = []
