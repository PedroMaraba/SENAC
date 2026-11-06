a1 = float(input('Digite a nota do primeiro aluno: '))
a2 = float(input('Digite a nota do segundo aluno: '))
a3 = float(input('Digite a nota do terceiro aluno: '))
a4 = float(input('Digite a nota do quarto aluno: '))

media = (a1 + a2 + a3 + a4) / 4

print(f'A MÉDIA É {media}')

if media > 7:
    print('APROVADO!')
elif media >= 5 and media <= 7:
    print('RECUPERAÇÃO!')
else: 
    print('REPROVADO!')

