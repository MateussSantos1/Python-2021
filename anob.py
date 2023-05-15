ano = int(input('Digite aqui um ano bissexto: '))
while ano % 4 != 0:
    ano = int(input('Digite um ano que seja BISSEXTO!!! '))
print('Obrigado!!! {} é um ano bissexto!!!'.format(ano))