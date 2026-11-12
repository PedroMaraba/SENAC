#USO DO MATCH CASE: 

#ANTES: IF/ELSE

# print('############## ATENDIMENTO OUTHERE #################')

# categorias = ['Massas', 'Bebidas', 'Doces', 'Petiscos', 'Salgados', 'Salgados', 'Pizza', 'Churrasco', 'Lanches', 'Comida Japonesa', 'Pastel']
# print(categorias)

# pergunta = input('Escolha ma das categorias abaixo: ')

# if pergunta == 'Massas':
#     print('Dia das Massas, com rodízio e descontos é toda quarta-feira!')

# elif pergunta == 'Bebidas':
#     print('Dia das bebidas, com rodízio e descontos é toda quarta-feira!')
    
# elif pergunta == 'Petiscos':
#     print('Dia dos petiscos, com rodízio e descontos é toda quarta-feira!')

# elif pergunta == 'Doces':
#     print('Dia dos doces, com rodízio e descontos é toda quarta-feira!')

# elif pergunta == 'Salgados':
#     print('Dia dos salgados, com rodízio e descontos é toda quarta-feira!')

# elif pergunta == 'Pizza':
#     print('Dia das pizzas, com rodízio e descontos é toda quarta-feira!')

# elif pergunta == 'Churrasco':
#     print('Dia dos churrascos, com rodízio e descontos é toda quarta-feira!')

# elif pergunta == 'Lanche':
#     print('Dia dos lanches, com rodízio e descontos é toda quarta-feira!')

# elif pergunta == 'Comida Japonesa':
#     print('Dia das Massas, com rodízio e descontos é toda quarta-feira!')

# elif pergunta == 'Pastel':
#     print('Dia dos pasteis, com rodízio e descontos é toda quarta-feira!')

# else: 
#     print('Opção inválida, tente novamente!')


print('############## ATENDIMENTO OUTHERE #################')

categorias = ['Massas', 'Bebidas', 'Doces', 'Petiscos', 'Salgados', 'Salgados', 'Pizza', 'Churrasco', 'Lanches', 'Comida Japonesa', 'Pastel']
print(categorias)

pergunta = input('Escolha ma das categorias abaixo: ')

match pergunta:
    case 'Massas':
        print('Dia das Massas, com rodízio e descontos é toda quarta-feira!')
    case _: 
        print('Categoria não encontrada!')
        