
# Dobro, Triplo, Raiz Quadrada
titulo = '\033[32m#006 \033[33m- Dobro, Triplo, Raiza Quadrada\033[m'
print(titulo)

n = float(input('\033[31mDigite um número: \033[m'))
print("\033[36mO dobro de \033[32;1m{}\033[m \033[36mvale \033[32;1m{}\033[m\033[36m\nO triplo vale \033[32;1m{}\033[m\033[36m\nE a raiz quadrada é \033[32;1m{:.2f}\033[m".format(n, (n * 2), (n * 3), (n ** (1 / 2))))
# Raiz quadrada na função de power: "pow(n, (1/2)", "n" seria a variavel/objeto
