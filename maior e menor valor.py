from time import sleep
a = float(input('Digite um valor:'))
b = float(input('Digite um segundo valor: '))
c = float(input('Digite um terceiro valor: '))
print('Só um momento....')
sleep(3)
print('Quase lá...')
sleep(3)
if b < a and b < c:
    print('{:.1f} é o menor entre os três!!! '.format(b))
if c < a and c < b:
    print('{:.1f} é o menor entre os três!!! '.format(c))
if a < b and a < c:
    print('{:.1f} é o menor!!!'.format(a))
else:
    print('Todos os valore são iguais!!!')