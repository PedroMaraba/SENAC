peixes = int(input('Quantos quilos de peixe trouxe: '))

def calcMult(peso):
    if peso > 100:
        pesoExcedido = peso - 100
        multa = pesoExcedido * 4
        return multa
    else:
        return 0
    
fim = 's'
while fim == 's':
    peixes = int(input('Quantos quilos de peixe trouxe: '))

    if calcMult(peixes) > 0:
        print(f'O valor da multa é {calcMult(peixes)}')
    else:
        print('Peso dentro do limite. Nenhuma multa para pagar.')
    fim = input('Deseja adicionar outra pesagem? ('s'ou 'n')')

