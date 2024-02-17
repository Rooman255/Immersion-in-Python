print("\nВведите стороны треугольника\n")

side_triangle_a = int(input("Сторона a = "))
side_triangle_b = int(input("Сторона b = "))
side_triangle_c = int(input("Сторона c = "))

if side_triangle_a + side_triangle_b > side_triangle_c and side_triangle_a + side_triangle_c > side_triangle_b and side_triangle_b + side_triangle_c > side_triangle_a:

    print("\nТреугольник с такими сторонами существует")

    if side_triangle_a != side_triangle_b and side_triangle_a != side_triangle_c and side_triangle_b != side_triangle_c:

        print("\nТакой треугольник назыается - Разносторонний\n")

    elif side_triangle_a == side_triangle_b and side_triangle_b == side_triangle_c:

        print("\nТакой треугольник назыается - Равносторонний\n")

    else:

        print("\nТакой треугольник назыается - Равнобедренный\n")

else:

    print("\nТреугольника с такими сторонами не существует\n")
