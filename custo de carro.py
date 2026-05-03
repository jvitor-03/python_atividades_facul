fabrica = float(input('Qual o seu preço de fabrica? '))
imposto = float(input('Qual o valor do imposto? '))
porcentagem =  float(input('Qual a porcentagem do distribuidor? '))
calculo = (imposto + porcentagem) / 100
calculo2 = fabrica * calculo
calculo3 = fabrica + calculo2
print(f'O custo é {calculo3}')
