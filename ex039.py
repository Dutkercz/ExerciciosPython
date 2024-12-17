import datetime

'''Faça um programa que leia o ano de nascimento de um jovem e informe, de
acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar
ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que
passou do prazo.'''

print('Primeiramente, diga seu sexo')
sexo=int(input('''1 - Masculino
2 - Feminino
-> '''))
if sexo == 2:
    print('Mulheres não precisam fazer o alistamento militar obrigatório!')
else:
    anoN = int(input('Qual seu ano de nascimento: '))
    anoA = datetime.date.today().year
    anot = anoA-anoN

    if anot == 18:
        print('Quem nasceu no ano de {}, completa 17 anos esse ano'.format(anoN))
        print('Portanto deve se alistar no Exército')
    elif anot < 18:
        anofut = (18 - anot) + anoA
        print('Quem nasceu no ano de {}, completa {} anos esse ano'.format(anoN, anot))
        print('Seu alistamento será em {}'.format(anofut))
    elif anot > 18:
        anopas = anoA - (anot - 18)
        print('Quem nasceu no ano de {}, completa {} anos esse ano'.format(anoN, anot))
        print('Seu alistamento foi em {}'.format(anopas))
        print('Você deveria ter se alistado há {} anos atrás !'.format(anoA-anopas))

