pot = int(input('Qual a potência da lâmpada? '))
larg = int(input('Largura: '))
comp = int(input('Comprimento: '))


m2 = larg * comp

m2ilum = m2 / 3


if pot < 3:
    print(f'Potência insuficiente para iluminar o cômodo.')
else:

    print(f'São necessárias {int(m2ilum)} lâmpadas')
    