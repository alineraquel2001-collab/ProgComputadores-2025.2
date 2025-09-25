#ATIVIDADE - CALCULAR AERA DO TRAPEZIO TRAPEZIO

print('Vamos calcular a area do trapesio!')

#VALOR DA BASE MAIOR
base_maior = input('Informe o valor da base maior do trapesio:')

#VALOR DA BASE MENOR
base_menor = input('Informe o valor da base menor do trapesio:')

#VALOR DA BASE MAIOR
altura = input('Informe o valor da altura do trapesio:')

base_maior = float(base_maior)
base_menor = float(base_menor)
altura = float(altura)

area = base_maior + base_menor * altura / 2

print(f'A area do trapezio é: {area}.')
