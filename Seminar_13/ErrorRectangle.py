class Error_side_a(Exception):
    def __init__(self, message="Число стороны 'a' не является целым числом"):
        self.message = message
        super().__init__(self.message)


class Error_side_b(Exception):
    def __init__(self, message="Число стороны 'b' не является целым числом"):
        self.message = message
        super().__init__(self.message)


class Error_side_a_not_null(Exception):
    def __init__(self, message="Значение для стороны 'a' не должно быть равно 0"):
        self.message = message
        super().__init__(self.message)


class Error_side_b_not_null(Exception):
    def __init__(self, message="Значение для стороны 'b' не должно быть равно 0"):
        self.message = message
        super().__init__(self.message)


class Error_side_a_negative_number(Exception):
    def __init__(self, message="Значение для стороны 'a' не должно иметь отрицатьльное число"):
        self.message = message
        super().__init__(self.message)


class Error_side_b_negative_number(Exception):
    def __init__(self, message="Значение для стороны 'b' не должно иметь отрицатьльное число"):
        self.message = message
        super().__init__(self.message)
