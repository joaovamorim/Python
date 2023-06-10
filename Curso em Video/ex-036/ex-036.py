# Aprovando Empréstimo

valor_da_casa = float(input('Qual o valor da casa: R$'))
salario_do_comprador = float(input('Qual o salário do comprador: R$'))
anos_a_pagar = int(input('Em quantos anos vai pagar: '))
prestação = valor_da_casa / (anos_a_pagar * 12)
minimo = salario_do_comprador * 30 / 100

print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}.'.format(valor_da_casa, anos_a_pagar, prestação))

if prestação <= minimo:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO.')
