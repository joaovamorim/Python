
# Pintando Parede
print('\033[32m#011 \033[34m- Pintando Parede\033[m')

largura = float(input('Largura da parede:\033[32m '))
altura = float(input('\033[mAltura da parede:\033[33m '))
area = largura * altura
print('\033[m\033[36mSua parede tem \033[97m{:.2f} \033[36mx \033[97m{:.2f}\033[36m, e sua área é de \033[97m{:.2f}\033[36mm².'.format(largura, altura, area))
tinta = float(area / 2)
print('Assim você precisaria de \033[97m{}\033[36mL de tintas para pintar esta área.\033[m'.format(tinta))
