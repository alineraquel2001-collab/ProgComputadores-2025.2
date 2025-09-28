#ATIVIDADE - CONVERSOR DE MOEDA

#USUARIO VAI DIGITAR O VALOR EM REAL
valorReais = float(input('Informe o valor em R$: '))

#USUARIO VAI DIGITAR O VALOR EM DOLAR
cotacaoDolar = float(input('Informe a cotação do dolar US$:'))

#CONVERTER REAL EM DOLAR
converter = valorReais / cotacaoDolar

#MOSTRA RESULTADO - REAL CONVERTIDO EM DOLAR
print(f'Com {valorReais} você poderá comprar aproxidamente US$ {converter:.2f}')

