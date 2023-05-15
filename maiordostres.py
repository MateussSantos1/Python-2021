n1, n2, n3 = input().split(" ")
n1 = int(n1)
n2 = int(n2)
n3 = int(n3)

if n1 > n2 and n1 > n3:
    print('{} é o maior dos três!!!'.format(n1))

if n2 > 1 and n2 > n3:
    print('{} é o maior dos três!!!'.format(n2))

else:
    print('{} é o maior dos três!!!'.format(n3))

