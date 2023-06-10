
from random import shuffle


aluno_1 = str(input('Nome do 1° Aluno: '))
aluno_2 = str(input('Nome do 2° Aluno: '))
aluno_3 = str(input('Nome do 3° Aluno: '))
aluno_4 = str(input('Nome do 4° Aluno: '))
lista = [aluno_1, aluno_2, aluno_3, aluno_4]
sorteio = shuffle(lista)
print('A ordem dos alunos será: \n{}'.format(lista))
