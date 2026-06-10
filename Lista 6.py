valores = [[], []]
valor = 0
for i in range(7):
    valor = int(input(f'Digite o {i +1} valor: '))
    if valor % 2 == 0:
        valores[0].append(valor)
    else:
        valores[1].append(valor)


valores[0].sort()
valores[1].sort()
print(f'Os valores pares são {valores[0]}')
print(f'Os valores ímpares são {valores[1]}')
   


    



 
