
from random import randint
from time import sleep


comp = randint(0, 5)
print('-=-' *20)
print('Vou pensar em um núemro entre 0 e 5 tente adivinhar')
print('-=-' *20)
jog = int(input('Em que número eu pensei: '))
print('PROCESSANDO...')
sleep(3)
if jog == comp:
    print('PARAÉNS VOCÊ ACERTOU!')
else:
    print('ERRADO! EU PENSEI NO NÚEMRO {}'.format(comp))
