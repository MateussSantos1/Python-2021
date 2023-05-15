l1 = float((input('Primeiro lado:  ')))
l2 = float(input('Segundo lado:  '))
l3 = float(input('Terceiro lado:  '))
if l1 == l2 == l3:
    print('EQUILATERO')
elif l1 != l2 and l2 != l3 and l1 != l2 and l2 != l3:
    print('ESCALENO')
else:
    print('ISÓSCELES')