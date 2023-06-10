
for m in range(7):
    ano = int(input('Ano de nascimento: '))
    idade = ano - 2023
    if (m == idade >= 21):
        m = m * m
        print('{}'.format(m)) 

