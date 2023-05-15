A, B, C = input().split(" ")
A = int(A)
B = int(B)
C = int(C)
tipo = 0
retan = 0
if (A + B) <= C:
 print('Invalido')
else:
    if( A==B and B==C):
        tipo = "Valido-Equilatero"
    elif (A ==B or B == C ):
        tipo = "Valido-Isoceles"
    else:
        tipo = "Valido-Escaleno"
        if ((pow(A, 2)+pow(B, 2))==pow(C, 2)):
            retan = "S"
        else:
            retan = "N"
print(tipo)
print("Retangulo: {}".format(retan))

