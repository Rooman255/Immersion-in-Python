import fractions

fraction_1_numerator = (input("Введите число в числитель первой дроби: "))
fraction_1_denominator = (input("Введите число в знаменатель первой дроби: "))
fraction_2_numerator = (input("Введите число в числитель второй дроби: "))
fraction_2_denominator = (input("Введите число в знаменатель второй дроби: "))


result_fraction_plus = int(fraction_1_numerator) / int(fraction_1_denominator) + \
    int(fraction_2_numerator) / int(fraction_2_denominator)
result_fraction_multiplication = int(fraction_1_numerator) / int(
    fraction_1_denominator) * int(fraction_2_numerator) / int(fraction_2_denominator)

print(result_fraction_plus)
print(result_fraction_multiplication)

fraction_1 = fractions.Fraction(
    int(fraction_1_numerator), int(fraction_1_denominator))
fraction_2 = fractions.Fraction(
    int(fraction_2_numerator), int(fraction_2_denominator))

fraction_plus = fraction_1 + fraction_2
fraction_multiplication = fraction_1 * fraction_2

print(fraction_plus)
print(fraction_multiplication)
