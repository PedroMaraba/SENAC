cont = 3
login = 'admin'
senha = 1234

print(f'Você tem {cont} tentativas.')
tentativaLogin = input('Digite o Login: ')
tentativaSenha = int(input('Digite a senha: '))


while (tentativaLogin != login or tentativaSenha != senha) and  cont > 1:
    cont = cont -1
    print(f'Login ou senha inválidos, restam {cont} tentativas')
    tentativaLogin = input('Digite o Login: ')
    tentativaSenha = int(input('Digite a senha: '))
if tentativaLogin == login and tentativaSenha == senha:
    print('Login realizado com sucesso!')
else:
    print('Número de tentativas excedido. Acesso bloqueado.')
