#CALCULO CAIXA DE AZULEJO
print('###DESCUBRA QUANTAS CAIXAS DE AZULEJO SERÃO NECESSÁRIAS!###')

# Definindo as variáveis

comp = int(input('Qual o comprimento da cozinha? '))
larg = int(input('Qual a largura da cozinha?'))
alt = int(input('Qual a altura da cozinha?'))
caixa = 1.5

#Fazendo os cálculos


# pega o metro quadrado de duas paredes 
primeira2paredes = 2 * larg * alt

# pega o metro quadrado de outras duas paredes
segunda2paredes = 2 * comp * alt

# soma os metros quadrado das duas paredes
m2total = primeira2paredes + segunda2paredes

#calcula quantas caixas de azulejo serão necessárias
resultado = m2total = m2total / caixa

if resultado != int(resultado):
    resultado = int(resultado) + 1
    print(f'Serão necessários {int(resultado)} caixas de azulejo, e irá sobrar alguns azulejos. ')
else:
    print(f'Serão necessários {int(resultado)} caixas de azulejo.')

