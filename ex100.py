from random import randint
from time import sleep


#ROTINAS
def sorteia(lisnum): #PEGOU a VAR E COLOCOU NO LUGAR DE 'LISNUM'
    for c in range (0, 5):
       lisnum.append(randint(1, 10)) #PREENCHEU A VAR 'LINUM' E DEVOLVE
    print('Os numeros sorteados foram: ')
    for c in lisnum:
       print(f'{c}', end=' ')
       sleep(0.4)
    print('FIM')


def somapar(num):
    somar = 0
    for c in num:
        if c % 2 == 0:
            somar += c
    print(f'A soma dos numeros pares da lista {num} é {somar}', flush=True)

#PROGRAMA PRINCIPAL

numeros = [] #VARIAVEL QUE IRA RECEBER OS NUMEROS DA MINHA FUNÇÃO

sorteia(numeros) #CHAMO A VAR 'NUMEROS' E JOGO PRA DENTRO DA FUNÇÃO PARA PREENCHELA

sleep(1.5)

somapar(numeros) #JOGO A VAR 'NUMEROS' JA PREENCHIDA E EXECUTA A FUNÇÃO
