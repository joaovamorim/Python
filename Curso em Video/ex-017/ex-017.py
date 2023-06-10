
from math import hypot

print('\033[32m#017 \033[34m- CATETOS E HIPOTENUSA')

co = float(input('\033[mComprimento do cateto oposto:\033[32m '))
ca = float(input('\033[mComprimento do cateto adjacente:\033[32m '))
hi = hypot(co, ca)
print('\033[mA hipotenusa vai medir: \033[32m{:.2f}'.format(hi))

'''hi = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai medir: {:.2f}'.format(hi))'''
