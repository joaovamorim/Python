
velocidade = float(input('Qual é a velocidade atual do carro? '))
if velocidade > 80:
    print('MULTADO!! você excedeu o limite de 80km/h')
    multa = (velocidade-80) * 7
    print('Você deve pagar uma multa de R${:.2f}'.format(multa))
print('Tenha um Bom dia, diriga ocm segurança!')
