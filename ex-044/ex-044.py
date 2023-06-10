
# Gerencioador de Pagamentos
print('\033[34m{:=^40}'.format(' LOJAS AMORIM '))

preço_compra = float(input('\033[37mPreço das Compras: R$\033[32m'))
print('''\033[32m*** FORMAS DE PAGAMENTO ***
\033[37m[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opção = int(input('Qual é a opção? '))

if opção == 1:
    total = preço_compra - (preço_compra * 10 / 100)
elif opção == 2:
    total = preço_compra - (preço_compra * 5 / 100)
elif opção == 3:
    total = preço_compra
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R$\033[32m{:.2f} SEM JUROS.\033[37m'.format(parcela))
elif opção == 4:
    total = preço_compra + (preço_compra * 20 / 100)
    total_parcelas = int(input('Quantas parcelas? '))
    parcela = total / total_parcelas
    print('Sua compra será parcelada em {}x de R$\033[32m{:.2f}\033[37m COM JUROS.'.format(total_parcelas, parcela))
else:
    total = preço_compra
    print('\033[31mOPÇÃO INVÁLIDA de pagamento. Tente novamente!')
print('\033[37mSua compra de R%\033[32m{:.2f}\033[37m vai custar R$\033[32m{:.2f}\033[37m no final.'.format(preço_compra, total))
