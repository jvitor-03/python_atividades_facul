n = []
for i in range(5):
    n.append(float(input('Digite algum valor')))

#print(f'O maior valor é {max(n)}')
#print(f'O menor valor é {min(n)}')
maior_valor = n[0]
posicao_maior = 0

menor_valor = n[0]
posicao_menor = 0

for indice, valor in enumerate(n):
    if valor > maior_valor:
        maior_valor = valor
        posicao_maior = indice

    if valor < menor_valor:
        menor_valor = valor
        posicao_menor = indice

print(f'O maior valor é {maior_valor} e a posição é {posicao_maior}')
print(f'O menor valor {menor_valor} e a posição é {posicao_menor}')
