from datetime import date
print('Classificação dos atletas por idade')
nasc = int(input('Qual o ano de nascimento do Atleta: '))
ano = date.today().year
idade = ano - nasc

if idade <= 9:
    print('Um atleta de {} anos, compete na categoria MIRIM'.format(idade))
elif idade > 9 and idade <= 14:
    print('Um atleta de {} anos, compete na categoria INFANTIL'.format(idade))
elif idade > 14 and idade <=19:
    print('Um atleta de {} anos, compete na categoria JUNIOR'.format(idade))
elif idade > 19 and idade <= 25:
    print('Um atleta de {} anos, compete na categoria SÊNIOR'.format(idade))
elif idade > 25:
    print('Um atleta de {} anos, compete na categoria MASTER'.format(idade))

