lista = []

while True:
    m = lista.append(int(input('Adicione um número: ')))
    b = str(input('Deseja sair? [S/N]'))
    if b in 'Ss':
        break

print(f'Foram {len(lista)} números  digitados ')
lista.sort()
print(lista)
if 5 in lista:
    print('Tem 5 na lista')
else:
    print('Não tem 5 na lista')
