print('Olá! Estou aqui para ajudá-lo a converter Reais para Dólar.')
cotacao_dolar = 5.20

reais = float(input('Qual valor em Reais (R$) você gostaria de converter? '))

total_dolar = reais / cotacao_dolar

print(f'Com R$ {reais:.2f}, você tem aproximadamente US$ {total_dolar:.2f}')
