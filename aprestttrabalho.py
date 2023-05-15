from random import  shuffle
n1, n2, n3, n4 = str(input('Digite aqui os nomes dos 4 componentes do grupo: ')).split(' ')
grupo = [n1, n2, n3, n4]
shuffle(grupo)
print('A ordem de apresentação será: ')
print(grupo)

