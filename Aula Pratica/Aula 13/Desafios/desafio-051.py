
print('Progressão aritimética - 10 primeiros termos.\n')

p_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão da PA: '))

print('\nOs 10 primeiros termos dessa PA:')
for i in range(0, 10):
    termo = p_termo + (razao * i)
    print(termo)
print('FIM')
