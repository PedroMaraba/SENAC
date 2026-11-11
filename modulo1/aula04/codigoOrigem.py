#PROGRAMA QUE INFORMA DE QUAL REGIAO É O CODIGO INFORMADO PEO USUÁRIO

codigo = int(input('Digite o código de origem do produto: '))

match codigo:
    case 1:
        print('a origem do produto é: Sul')
    case 2:
        print('a origem do produto é: Norte')
    case 3:
        print('a origem do produto é: Leste')
    case 4:
        print('a origem do produto é: Oeste')
    case 5:
        print('a origem do produto é: Nordeste')
    case 6:
        print('a origem do produto é: Sudeste')
    case 7:
        print('a origem do produto é: Centro-Oeste')
    case 8:
        print('a origem do produto é: Noroeste')

    case _:
        print('Produto importado. ')
        

