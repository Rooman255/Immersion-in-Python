import math
import csv
import json
import random
import functools


class Decorators:

    def __init__(self, variable_a, variable_b, variable_c):

        self.variable_a = variable_a
        self.variable_b = variable_b
        self.variable_c = variable_c

    def from_csv_decorator(func):

        @functools.wraps(func)
        def wrapper():

            results = []

            with open("number.csv", mode='r') as file_csv:

                reader = csv.reader(file_csv)

                for row in reader:

                    variable_a, variable_b, variable_c = map(int, row)

                    results.append(func(variable_a, variable_b, variable_c))

            return results

        return wrapper

    def find_roots(variable_a, variable_b, variable_c):

        discriminant = variable_b * variable_b - 4 * variable_a * variable_c
        square_value = math.sqrt(abs(discriminant))
        if discriminant > 0:
            x1 = (-variable_b + square_value) / (2 * variable_a)
            x2 = (-variable_b - square_value) / (2 * variable_a)
            return (x1, x2)

        elif discriminant == 0:

            x1 = -variable_b / (2 * variable_a)
            return (x1)

        else:

            x1 = - variable_b / (2 * variable_a), " + i", square_value
            x2 = - variable_b / (2 * variable_a), " - i", square_value
            return (x1, x2)

    def csv_generate(file_name):

        with open(file_name, 'w', newline='') as file_csv:

            writer = csv.writer(file_csv)

            for i in range(random.randint(100, 1001)):

                writer.writerow([random.randint(1, 100) for j in range(3)])

    def log_decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            with open('info.json', 'a') as f:
                json.dump({'func': func.__name__, 'args': args,
                           'kwargs': kwargs, 'result': result}, f)
            return result
        return wrapper


if __name__ == "__main__":

    file_name = "number.csv"

    Decorators.csv_generate(file_name)

    print(
        f"\nФайл {file_name} с тремя случайными числами в каждой строке, сгенерирован!\n")

    f = Decorators.from_csv_decorator(Decorators.find_roots)
    f()

    print(f"\nДекоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла. С работал!\n")

    log_dec = Decorators.log_decorator(f)
    log_dec()

    print(f"\nДекоратор, сохраняющий переданные параметры и результаты работы функции в json файл. С работал!\n")
