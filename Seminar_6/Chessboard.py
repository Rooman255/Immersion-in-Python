import random
from copy import copy


class Chessboard:
    def __init__(self, length: int):
        self.length = length
        self.board = []
        self.all_variants = []
        self.queen_position(0)

    def queen_placement(self, row: int, num: int):
        for i, value in enumerate(self.board):
            if value == num or (i - row) == (value - num) or (i - row) == (num - value):
                return False
        return True

    def queen_position(self, row: int):
        if row == self.length:
            self.all_variants.append(copy(self.board))
        else:
            for col in range(self.length):
                if self.queen_placement(row, col):
                    self.board.append(col)
                    self.queen_position(row + 1)
                    self.board.pop()

    def position_check(self, board: list[int]):
        return board in self.all_variants


def random_positions_get(board=[0, 1, 2, 3, 4, 5, 6, 7]):
    random.shuffle(board)
    return board


if __name__ == '__main__':
    board_size = 8
    boards = Chessboard(board_size)
    print(f"\nГенератор случайных чисел для случайной расстановки ферзей\n{boards.all_variants}\n")
    get_value_from_player = [0] * board_size
    print("Введите 8 пар чисел")
    for count in range(board_size):
        row, col = (int(i) - 1 for i in input(f"{count + 1} пара. Вводим через пробел два значения от 1 до 8 для позции Ферзя: ").split(" "))
        get_value_from_player[col] = row
    print(get_value_from_player)
    print(boards.position_check(get_value_from_player))
    count = 0
    while count < 4:
        random_positions_on_board = random_positions_get()
        if boards.position_check(random_positions_on_board):
            print(random_positions_on_board)
            count += 1
