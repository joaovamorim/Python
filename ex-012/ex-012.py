
# Calculando Descontos
print('\033[32m#012 \033[33m- CALCULANDO DESCONTOS')

pc = float(input('Qual é o preço do produto: R$\033[32m'))
re1 = pc -  (pc * 5 / 100)
print('\033[97mO produto R$\033[32m{:.2f}\033[97m com 5% de desconto na promoção vale R$\033[32m{:.2f}\033[m'.format(pc, re1))
