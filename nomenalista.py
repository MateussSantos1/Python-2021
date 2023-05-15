import random

n1, n2, n3, n4 = str(input('Digite o nome de 4 alunos respectivamente:')).split(' ')
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print('O aluno escolhido foi o: {}'.format(escolhido))
