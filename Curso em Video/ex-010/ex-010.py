
# Conversor de Moedas
print('\033[32m#010\033[33;1m - Conversor de Medidas\033[m')

brl = float(input('\033[36mQuanto dinheiro você tem na carteira? \033[32mR$\033[m'))
usd = brl * 0.20
print('\033[33mCom \033[32mR${:.2f} \033[33mvocê pode comprar \033[32;1mUS${:.2f}\033[m'.format(brl, usd))
