vel = float(input('Digite aqui asua velocidade em KM/h: '))
ult = (vel - 80) * 7
if vel <= 80:
    print('Boa viagem, continue respeitando as normas de trânsito!!!')
elif vel > 80:
    print('Ops, parece que você está com a velocidade acima da permitida!!!')
    print('Você pagará uma multa de R$ {:.2f} por sua infração!!!'.format(ult))
