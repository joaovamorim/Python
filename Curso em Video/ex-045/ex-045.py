
# Jogo Pedra Papel Tesoura
from random import randint
from time import sleep



print('{:=^40}'.format(' Jogue comigo Pedra, Papel, Tesoura '))

itens = ('\033[37mPedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Sua opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é sua a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')

print('=' * 25)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('=' * 25)

if computador == 0: # Computador Jogou PEDRA
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 1: # Computador Jogou PAPEL
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 2: # Computador Jogou TESOURA
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA!')
