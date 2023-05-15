'''ano = int(input('Digite aqui um ano, para saber se ele é bissexto: '))
if ano % 4 == 0:
    print ('Ele é bissexto!!!')
else:
    print("Não, ele não é bissexto!!!")'''
from time import sleep
n = 1
while n % 4 != 0:
    n = int(input('Digite aqui um ano bissexto: '))
print('Parabéns! {} é um ano bissexto!'.format(n))
co = str(input('Deseja continuar ??? S/N')).strip().upper()
if co == "S":
    n = 1
    while n % 4 != 0:
        n = int(input('Digite aqui um ano bissexto: '))
    print('Parabéns! {} é um ano bissexto!'.format(n))
    co = str(input('Deseja continuar ??? S/N')).strip().upper()
if co == "N":
    print('Tá bem, obrigado1!!! :)')
else:
    print("Se liga meo, escreve certo si nao da errado '-'")
    co = str(input('Deseja continuar ??? S/N')).strip().upper()
    if co == "S":
        n = 1
        while n % 4 != 0:
            n = int(input('Digite aqui um ano bissexto: '))
        print('Parabéns! {} é um ano bissexto!'.format(n))
        co = str(input('Deseja continuar ??? S/N')).strip().upper()
    if co == "N":
        print('Beleza ;(')
    else:
        print('Beleza, vlw  ;( ')
        sleep(2)
        novo = str(input('Vai diz aí, s ou n???')).upper()
        if novo == "S":
            n = 1
            while n % 4 != 0:
                n = int(input('Digite aqui um ano bissexto: '))
            print('Parabéns! {} é um ano bissexto!'.format(n))
            novo = str(input('Deseja continuar ??? S/N')).strip().upper()
        if novo == "N":
            print('Tá bem, obrigado1!!! :)')
        else:
            print("Se liga meo, escreve certo si nao da errado '-'")
           




