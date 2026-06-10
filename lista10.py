lista = []
soma = 0
for i in range(5):
    valor = int(input('Adicione um valor: '))
    lista.append(valor)
    soma += valor

media = soma / 5
print(lista)
print(f'A média desses valores é {media}')
