lista = list()
lista_validos = list()

for i in range(5):
    idade = int(input('Idade: '))
    if idade < 18:
        print('Não pode participar.')
    else:
        lista.append(idade)
        nome = input('Informe o nome')
        lista.append(input('Informe o email: '))
        lista.append(input('Informe o telefone: '))
        dic = dict()
        dic[nome] = lista.copy()
        lista_validos.append(dic)
        lista.clear()


print(lista_validos)