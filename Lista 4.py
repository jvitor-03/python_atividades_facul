lista = []
impares = []
pares = []
while True:
    m = lista.append(float(input('Adicione um número: ')))
    k = str(input('Deseja sair? [S/N]' ))
    if k in 'Ss':
            break

for i, v in enumerate(lista):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)

print(f'Lista completa {lista}')
print(f'Apenas os pares é {pares}')
print(f'Apenas os ímpares é {impares}')
