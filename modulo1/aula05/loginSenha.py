cont = 3
login = 'admin'
senha = 1234

print(f'Você tem {cont} tentativas.')
tentativaLogin = input('Digite o Login: ')
tentativaSenha = int(input('Digite a senha: '))


while tentativaLogin != login and tentativaSenha != senha:
    cont = cont -1
    if cont  > 0:
        print(f'Login ou senha inválidos, restam {cont} tentativas')
        tentativaLogin = input('Digite o Login: ')
        tentativaSenha = int(input('Digite a senha: '))
    else:
        break
print('login concluído!')