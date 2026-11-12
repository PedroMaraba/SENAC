   
for i in range(2):
    Nome = input(f'Digite o nome do {i + 1}° aluno: ')
    notaAva1 = int(input('Digite a nota da primeira avaliação: '))
    notAva2 = int(input('Digite a nota da segunda avaliação: '))
    notaOpt= int(input('Digite a nota davaliação optativa, caso não tenha feito, digite "-1": '))

    print(f'Aluno: {Nome}')

    if notaOpt == -1:
        media = (notaAva1 + notAva2 ) / 2
        if media < 3:
            print('Reprovado!')
        elif media >=3 and media <= 6:
            print('Recuperação!')
        else: 
            print('Aprovado!')

        print(f'A MÉDIA É {media}')

    else: 
        if notaAva1 > notAva2: 
            media = (notaAva1 + notaOpt) / 2
            print(f'A MÉDIA É {media}')
        elif notaAva1 == notAva2:
            media = (notaAva1 + notaOpt) / 2
            print(f'A MÉDIA É {media}')
        else: 
            media = (notAva2 + notaOpt) / 2
            print(f'A MÉDIA É {media}')