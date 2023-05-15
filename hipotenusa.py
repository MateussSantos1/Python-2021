co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o cateto adjacente: '))
hip = (co ** 2 + ca ** 2) ** (1/2)
print('O valor da hipotenusa será: {:.2f}'.format(hip))