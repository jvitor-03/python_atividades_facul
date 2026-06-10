lista = []
while True:
    lista.append(int(input('Digite um número: ')))
    g = input('Deseja continuar? [S/N]')
    if g in 'Nn':
        break
lista.reverse()
print(lista)
