'''qtd = int(input(''))
h = (('Ho '* (qtd -1)))
print('{}Ho!'.format(h))'''
comeco = 0
numero = int(input(''))

'''oxi = "N[{}]= {}".format(comeco, numero)
print (oxi)

if numero < 50:
    for c in range(1,11):
        cce = comeco+ c
        oxxxe = (c -1) * 4
        print("N[{}] = {}".format(c,oxxxe ))'''

'''n = int(input())
x=0
maior = 0
posicao = 0
for i in range(1,100):
    a = int(input())
    if a > x:
        maior = a
        posicao = i + 1
        x = a

print(maior)
print(posicao)

l = 0
while l != 0:
    l = list(map(int, input().split()))

print(max(l))'''


'''i =0
n = 0

while (int(n[i]) != 0):
    n = input().split()
    lista = []
    lista.append(int(n[1]))
'''

n = input().split()
lista = []

i = 0

while (int(n[i]) != 0):
    lista.append(int(n[i]))
    i += 1
print(max(lista))