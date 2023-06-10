
# Respondendo ao Usuário
from traceback import print_tb


titulo = '\033[32m#002 \033[31m- Respondendo ao Usuário\033[m'
print(titulo)

nome = input('\033[7mQual é o seu nome? ')
print('\033[m\033[34;1;4mOlá, Prazer em conhece-lo {}!\033[m'.format(nome))
