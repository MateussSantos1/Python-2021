'''contador  = 1
while contador <= 10:
    print(contador,'-> ', end=" ")
    contador = (contador + 1)
print('Acabou')'''

contador  = 0
while True:
    for c in range(0,11):
        print(contador,'-> ', end=" ")
        contador = (c + 1)
    if contador == 11:
        break
print('Acabou !!!')


