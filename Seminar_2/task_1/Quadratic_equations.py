value_1 = float(input('Введите первое значение: '))
value_2 = float(input('Введите второе значение: '))
value_3 = float(input('Введите третье значение: '))

discriminant = value_2 ** 2 - 4 * value_1 * value_3

if discriminant > 0:

    x_1 = (-value_2 + discriminant ** 0.5) / (2 * value_1)
    x_2 = (-value_2 - discriminant ** 0.5) / (2 * value_1)

    result = f'Для этого уравнения существует два корня, это {x_1 = } и {x_2 = }'

elif discriminant == 0:

    x = -value_2 / (2 * value_1)

    result = f"Для этого уравнения существует один корень, это {x = }"

else:

    discriminant = complex(discriminant, 0)

    x_1 = (-value_2 + discriminant ** 0.5) / (2 * value_1)
    x_2 = (-value_2 - discriminant ** 0.5) / (2 * value_1)

    result = f'Для этого уравнения существует два комплексных корня, это {x_1 = } и {x_2 = }'

print(result)
