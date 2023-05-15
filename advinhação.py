from random import randint
from time import sleep

computador = randint(0, 5) #Faz o computador pensar#
print('*' * 20)
print('Vou pensar em um número entre 0 e 5, tente advinhar....')
print('*' * 20)
jogador = int(input('Em que número eu pensei ??? ')) #Jogador tenta advinhar

if  jogador == computador:
    print('PROCESSANDO...')
    sleep(3)
    print('PARABÉNS, você me venceu!!!')
else:
    print('PROCESSANDO...')
    sleep(3)
    print('Haha, eu ganhei, eu pensei no número {}, e não no número {}. Tente novamente :)'.format( computador, jogador))




