for c in range(0,10):
    n = int(input())
    i = 0
    if n == 0:
        i =1
        print('X[{}] = {}'.format(c, i))
    if n < 0:
        i = 1
        print('X[{}] = {}'.format(c,i))
    if n > 0:
        i = n
        print('X[{}] = {}'.format(c,i))