
distancia = float(input('Qual é a distancia de sua viagem? '))
print('Você está prestes a começar uma viagem de {}Km'.format(distancia))

'''if distancia <= 200:
    preco = distancia * 0.50
else:
    preco =distancia * 0.45'''

preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print('E o preço de sua biagem será de R${:.2f}'.format(preco))
