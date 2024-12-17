def lin(tex):
    print('-=-'*20)
    print(f'{tex:^50}')
    print('-=-'*20)


def soma(a,b):
    print(f'o valor a é {a} e o valor b é {b}')
    s=a+b
    print(s)


lin('Curso em Video')
soma(2,5) #podemos explicitar qual o valor de cada um, exp. soma(a=5, b=2)
soma(b=5, a=2)
soma(9,2)
lin('fim da aula')

'''EMPACOTAMENTO DE PARAMETROS'''

def contador (*numero): #para poder passar infinitos numeros usamos o *
    print(f' Os numeros são {numero}')
    print(f'Temos ao todos {len(numero)} numeros')
    print(f' A soma é {sum(numero)}')
    for c in numero:
        print(c)
lin('mais aulas')

contador(2,3,4,5,)

'''TRABALHANDO COM LISTA'''

def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


lista = [2, 3, 6, 7]
dobra(lista)
print(lista)