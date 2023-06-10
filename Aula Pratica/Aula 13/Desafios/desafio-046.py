
# Contagem regressiva de 10 a 0 a cada 1 segundo
from time import sleep

print('Feliz Ano NOVO, Vamos Contar de 10 a 0?')


for tempo in range(11, 0, -1):
    sleep(1)
    tempo -= 1
    print(tempo)
print('FELIZ ANO NOVO!!!')
