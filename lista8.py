lista = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = soma_par = maior = 0
for i in range(3):
    for j in range(3):
        lista[i][j] = int(input('Adicione um valor: '))
for i in range(3):
    for j in range(3):
        print(f'[{lista[i][j]}]', end='')
        if lista[i][j] % 2 == 0:
            soma_par += lista[i][j]
    print()
print(f'A soma dos pares é {soma_par}')
for i in range(3):
    soma += lista[i][2]
print(f'A soma dos valores da terceira columa são {soma}')
for j in range(3):
    if j == 0:
        maior = lista[1][j]
    elif lista[1][j] > maior:
        maior = lista[1][j]
print(f'O maior numero da segunda linha é {maior}')
