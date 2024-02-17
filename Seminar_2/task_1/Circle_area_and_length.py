import math
import decimal


decimal.getcontext().prec = 42

PI = decimal.Decimal(math.pi)


diameter = decimal.Decimal(input('Введите диаметр круга от 1 до 1000: '))

if diameter > 0 and diameter < 1001:

    circumference = PI * diameter
    area_circle = PI * (diameter / 2) ** 2

    print(f'Длина окржности = {circumference}')
    print(f'Площадь круга = {area_circle}')

else:
    print(
        f"Извените есть ограничения ввода значений от 1 до 1000, а Вы ввели {diameter}, будте внимательны")
