sal = float(input('Digite o seu salário aqui:'))
if sal <= 1250:
    nosal = sal + (15/100 * sal)
    print('De acordo com as novas regras da empresa, o sue novo salário será: R${:.2f}'.format(nosal))
if sal >= 1250:
    nosal = sal + (10/100 * sal)
    print('De acoroo com as novas regras da empresa, o seu novo salário será R${:.2f}'.format(nosal))