'''def mostraLinha ():
    print('--' * 30)

mostraLinha()
print('                 sistema')
mostraLinha()
print('                 user')
mostraLinha()
print('                 error')'''

'''def mostraLinha ():
    print('--' * 30)
def mensagem (msg):
    print('--' * 30)
mensagem('SISTEMA DE ALUNOS')
mostraLinha()
msg
mostraLinha()

mostraLinha()'''



'''def titulo(txt):
    print('-' * 30)
    print(txt)
    print('-' * 30)


#Progama Principal
titulo('   Curso em video   ')
titulo('   Aprenda Python   ')
titulo('        FLA   ')'''


'''a = int(input('Digite um valor: '))
b = int(input('Digite outro valor: '))
def soma(a,b):
    s = a + b
    print('A soma de {} + {} tem como resultado o valor {}'.format(a,b,s))

#Progama Principal:

soma(a,b)'''



def contador(*num):
    print(num)
    print(len(num))
    for valor in num:
        print('   {}   '.format(valor), end = '')
    print('FIM!!!')

contador(2,3,543,4)
contador(0,1)





