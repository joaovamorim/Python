
# Método 1 menos simplificado

print('MÉTODO 1')
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
juntos = ''.join(palavras)
inverso = ''

print('Você digitou a frase {}'.format(juntos))
for letra in range(len(juntos) - 1, -1, -1):
    inverso += juntos[letra]
print('O inverso de {} é {}'.format(juntos, inverso))

if inverso == juntos:
    print('Temos um PALINDROMO!')
else:
    print('A frase digitada NÃO é um PALINDROMO!')

# Método 2 mais simplificado

'''print('MÉTODO 2')
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
juntos = ''.join(palavras)
inverso = juntos[::-1]

print('Você digitou a frase {}'.format(juntos))
print('O inverso de {} é {}'.format(juntos, inverso))

if inverso == juntos:
    print('Temos um PALINDROMO!')
else:
    print('A frase digitada NÃO é um PALINDROMO!')
'''