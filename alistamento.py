nasc = int(input('Digite aqui o seu ano de nascimento: '))
ano = int(input('Digite aqui o ano atual: '))
idade = ano - nasc
anual = nasc + 18
atraso = ano -  (anual)
if idade  == 18 :
    print('Você deve se alistar IMEDIATAMENTE !!! por favor, dirija -se ao quartel mais próximo de sua residência.')
elif idade < 18:
    print('Você ainda tem {} anos, por isso deverá se alistar somente em {}'.format(idade, anual))
elif idade > 18:
    print('O senhor tem noção de tempo, 002? Deveria ter se alistado no ano de {}, ou seja, tem um atraso aproximado de {} anos. Por favor, se dirija a unidade mais próxima ;('.format(anual, ano - anual))
