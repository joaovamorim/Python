
# Reajuste Salarial
print('\033[32m#013 \033[m- REAJUSTE SALARIAL')

sal = float(input('\033[34mQual o seu salario para o aumento de 15%? R$\033[32m'))
conta = sal + (sal * 15 / 100)
print('\033[97mO seu salario de \033[32m{:.2f} \033[97maumentou para \033[32m{:.2f}\033[m'.format(sal, conta))
