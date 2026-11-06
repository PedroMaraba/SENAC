print('CALCULADORA')

n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))

soma = n1 + n2
subtracao = n1-n2
multiplicacao = n1 * n2
divisao = n1 / n2
moduloN1 = (n1 * n1) ** 0.5
# ou: moduloN1 = abs(n1)
moduloN2 = (n2 * n2) ** 0.5
# ou: moduloN1 = abs(n2)
moduloPython = n1 % n2

print(f'Soma: {soma}\nSubtração: {subtracao}\nMultiplicação: {multiplicacao}\nDivisão: {divisao}\nMódulo do primeiro número: {moduloN1}\nMódulo do segundo número: {moduloN2}\nResto da divisão: {moduloPython}')
