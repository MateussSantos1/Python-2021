n = 0
soma = cont = 0
while True:
    n = int(input('Digite um valor (999 para parar): '))
    if n == 999:
        break
    cont = cont + 1
    soma = soma + n
print('A soma dos {} valores é igual a {} !!! '.format(cont, soma))
print('Fim !')

if a > b and a > c and a > d and a > e:
    return a
if b > a and b > c and b > d and b > e:
    return b

if c > a and c > b and c > d and c > e:
    return c
if d > a and d > b and d > c and d > e:
    return d
else:
    return e