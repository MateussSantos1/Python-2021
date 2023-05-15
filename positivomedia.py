soma = 0
quantidade = 0
valor = float(input())
if valor > 0:
    soma = soma + valor
    quantidade = quantidade + 1

    valor = float(input())
    if valor > 0:
        soma = soma + valor
        quantidade = quantidade + 1

valor = float(input())
if valor > 0:
    soma = soma + valor
    quantidade = quantidade + 1

valor = float(input())
if valor > 0:
    soma = soma + valor
    quantidade = quantidade + 1

valor = float(input())
if valor > 0:
    soma = soma + valor
    quantidade = quantidade + 1

valor = float(input())
if valor > 0:
    soma = soma + valor
    quantidade = quantidade + 1

print('{} valores positivos'. format(quantidade))
print ('{:.1f}'.format( soma/quantidade ))

