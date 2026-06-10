lista = []
while True:
    num = int(input('Digite um numero: '))
    if num not in lista:
              lista.append(num)
              print('Valor adicionado')
    else:
        print('Valor duplicado, não é possível adicionar')
    continuar = str(input('Vc quer continuar? [S/N]'))
    if continuar in 'Nn':
        break

lista.sort()
print(f'Esses são os valores digitados {lista}')
