

def lin (msg):
    print('=='*20)
    print(f'{msg:^40}')
    print('=='*20)


def area():
    l = float(input('Digite a largura do terreno: (m) '))
    c = float(input('Digite o comprimento do terreno: (m) '))
    total = l * c
    print(f'A área total do terreno é {total}m²:')

#PROGRAMA PRINCIPAL!
lin('CONTROLE DE TERRENOS')
area()