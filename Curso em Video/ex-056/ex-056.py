# Calculo da media da idade das pessoas
soma_idade = 0
media_idade = 0

# Analise do nome do homem mais velho
maior_idade_homem = 0
nome_homem_velho = ''

# Total de Mulheres com menos de 20 anos
total_mulher20 = 0

# Condições
for pessoa in range(1, 5):
    print('------ {}° Pessoa ------'.format(pessoa))
    nome = str(input('Nome da {}° Pessoa: '.format(pessoa))).strip()
    idade = int(input('Idade da {}° Pessoa: '.format(pessoa)))
    sexo = str(input('Sexo M/F: ')).strip ()
    soma_idade += idade
    if pessoa == 1 and sexo in 'Mm':
        maior_idade_homem = idade
        nome_homem_velho = nome
    if sexo in 'Mm' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_homem_velho = nome
    if sexo in 'Ff' and idade < 20:
        total_mulher20 += 1

media_idade = soma_idade / 4
# Resultado
print('A média de idade é: {}'.format(media_idade))
print('O Homem mais velho tem {} anos e se chama {}.'.format(maior_idade_homem, nome_homem_velho))
print('Ao todo são {} mulhere(s) com menos de 20 anos.'.format(total_mulher20))
