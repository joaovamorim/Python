
# from math import radians, sin, cos, tan
import math


angulo = float(input('Digite um angulo que desejas: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print('O angulo {} tem o SENO de {:.2f}'.format(angulo, seno))
print('O angulo {} tem o COSSENO de {:.2f}'.format(angulo, cosseno))
print('O angulo {} tem a TANGENTE de {:.2f}'.format(angulo, tangente))
