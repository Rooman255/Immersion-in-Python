from ErrorRectangle import Error_side_a, Error_side_b, Error_side_a_not_null, Error_side_b_not_null, Error_side_a_negative_number, Error_side_b_negative_number


class Rectangle:

    def __init__(self, side_a: int, side_b: int = None):

        if side_a != int(side_a):
            raise Error_side_a()
        if side_b != int(side_b):
            raise Error_side_b()

        if side_a == 0:
            raise Error_side_a_not_null()
        if side_b == 0:
            raise Error_side_b_not_null()

        if side_a < 0:
            raise Error_side_a_negative_number()
        if side_b < 0:
            raise Error_side_b_negative_number()

        self.side_a = side_a
        self.side_b = side_b if side_b is not None else side_a

    def perimeter(self):

        return 2 * (self.side_a + self.side_b)

    def area(self):

        return self.side_a * self.side_b

    def __add__(self, other):

        other_perimeter = self.perimeter() + other.perimeter()
        other_side_a = self.side_a
        other_side_b = other_perimeter / 2 - other_side_a

        return Rectangle(other_side_a, other_side_b)

    def __sub__(self, other):

        other_perimeter = abs(self.perimeter() - other.perimeter())
        other_side_a = min(
            [self.side_a, self.side_b, other.side_a, other.side_b])
        other_side_b = other_perimeter / 2 - other_side_a

        return Rectangle(other_side_a, other_side_b)


if __name__ == '__main__':

    rectangle_1 = Rectangle(10, 30)
    rectangle_2 = Rectangle(45, 30)

    resultSum = rectangle_1 + rectangle_2
    print(f"\n{resultSum.side_a, resultSum.side_b}")

    resultSub = rectangle_1 - rectangle_2
    print(f"\n{resultSub.side_a, resultSub.side_b}\n")
