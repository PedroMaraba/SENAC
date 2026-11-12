# Calcular rendmento do taxista

#definindo variaveis iniciais

valorGasolina = 6.5
quilometroInicial = float(input('Qual o valor do odometro no início do dia? '))
quilometroFinal = float(input('Qual o km total rodado no dia? '))
dinheiroRecebido = float(input('Qual o total recebido pelos passageiros? '))
litrosGasolina = int(input('Quantos abasteceu de gasolina ao longo do dia? '))

#calculos

#calculando os quilometros rodados ao longo do dia
quilometrosRodados = quilometroFinal - quilometroInicial

#Calculando o valor de gasolina gasto ao longo do dia
gasolinaGasta = litrosGasolina / valorGasolina

# calculando a media do consumo de gasolina durante o dia
mediaGasolina = quilometrosRodados / litrosGasolina

#calculando o lucro liquido do taxista
lucroLiquido = dinheiroRecebido - litrosGasolina * valorGasolina 

# imprimindo o rendimento para o usuário
print(f'O consumo de gasolina por quilometro é de {mediaGasolina}, e o lucro líquido do dia é:R${lucroLiquido}')
