print(f'\n{"-" * 60}')

for i in range(2, 11):
    for j in range(2, 6):
        print(f'{j} * {i} = {i * j}', end='\t')
    print()

print()

for i in range(2, 11):
    for j in range(6, 10):
        print(f'{j} * {i} = {i * j}', end='\t')
    print()

print(f'{"-" * 60}\n')
