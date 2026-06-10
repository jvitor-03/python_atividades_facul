temp = []
tudo = []
mai = men = 0
while True:
    temp.append(input('Digite o nome: '))
    temp.append(float(input('Digite o peso: ')))
    if len(tudo) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
        
    tudo.append(temp[:])
    temp.clear()
    c = input('Deseja Continuar? [S/N]')                           
    if c in 'Nn':
        break
print(f'Foram {len(tudo)} pessoas cadastradas')
print(f'O mais pesado com {mai} Kg')
for p in tudo:
    if p[1] == mai:
        print(f'{p[0]}')
print(f'O mais leve com {men} Kg')
for p in tudo:
    if p[1] == men:
        print(f'{p[0]}')
