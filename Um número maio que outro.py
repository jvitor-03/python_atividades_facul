num1 = int(input('Digite um número inteiro: '))
num2 = int(input('Digite um outro número inteiro: '))

if num1 > num2:
           print(f'O número {num1} é maior que o {num2}')
elif num2 > num1:
    print(f'O número {num2} é maior que o número {num1}')
else:
    print('Os números são iguais')
