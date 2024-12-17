from time import sleep
from random import randint

print('-=-'*20)
print('               JOGO DA ADIVINHAÇÃO ')
print('-=-'*20)
sleep(1)
num=randint(0,10)
print('       ESTOU PENSANDO EM UM NÚMERO ENTRE 0 e 10')
print('__'*30)
sleep(2)
print('Escolha um número e tente me vencer!!!')
escolha=int(input('Diga sua escolha ... '))
sleep(1)
print('Você escolheu {} !'.format(escolha))
sleep(1)
print('QUE RUFEM OS TAMBORES !')
sleep(1)
print('........')
sleep(1)
print('.....')
sleep(1)
print('...')
sleep(1)
if escolha==num:
    print('VOCE GANHOU! Eu estava pensando no {} mesmo!'.format(escolha))
else:
    print('VOCE PERDEU! Eu estava pensando no {}'.format(num))