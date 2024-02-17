symbol_space = ' '
symbol_star = '*'

how_many_rows = int(input("\nСколько рядов у ёлки? "))

print()

symbol_spaces = how_many_rows - 1
symbol_stars = 1

for i in range(how_many_rows):

    print(f'{(symbol_space * symbol_spaces) + (symbol_star * symbol_stars) + (symbol_space * symbol_spaces)}')

    symbol_stars += 2
    symbol_spaces -= 1

print()
