n = int(input('Digite um numero, para saber sua tabuada: '))
for c in range(-1,10,):
    print(' {} x {} = {}'.format(n, c + 1 , n * ( c + 1) ))