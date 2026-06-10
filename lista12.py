lista = []
for i in range(10):
    valor = int(input('Adicione um num: '))
    
    while valor in lista:
        valor = int(input('Valor duplicado, digite outro: '))

    lista.append(valor)

print(lista)
