lista = [[0, 0, 0 ], [0, 0, 0 ], [0, 0, 0 ]]
for i in range(3):
    for j in range(3):
        lista[i][j] = int(input(f'Dgite um número: '))

for i in range(3):
    for j in range(3):
        print(f'[{lista[i][j]}]', end='')
    print()
