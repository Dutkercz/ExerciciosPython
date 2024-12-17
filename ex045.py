import random
from time import sleep

print('=-='*15)
print('{:=^53}'.format('\033[31mPEDRA PAPEL TESOURA\033[m'))
print('=-='*15)
p='PEDRA'
t='TESOURA'
pa='PAPEL'
lista=(p, pa, t)

pcesco=random.choice(lista)

print('VAMOS JOGAR')
print('''          
[0]PEDRA 
[1]PAPEL 
[2]TESOURA
''')
esco=int(input('Qual você escolhe: '))


print('PEEEDRA')
sleep(1)
print('PAPEEEEL')
sleep(1)
print('TEEESOOOUUURAAAA!!')
sleep(1)
print('Você escolheu \033[34m{}\033[m. O PC escolheu \033[31m{}\033[m!'.format(esco(lista(esco)), pcesco), end='\n\n    ')

if pcesco==p:
    if esco=='PEDRA':
        print('\033[33mDESSA VEZ EMPATAMOS!\033[m')
    elif esco == 'PAPEL':
        print('\033[32mVOCÊ GANHOU!\033[31')
    elif esco == 'TESOURA':
        print('\033[31mO PC GANHOU')
    else:
        print('OPÇÃO INVÁLIDA')
elif pcesco== pa:
    if esco=='PAPEL':
        print('\033[33mDESSA VEZ EMPATAMOS!\033[m')
    elif esco == 'TESOURA':
        print('\033[32mVOCÊ GANHOU!\033[31')
    elif esco == 'PEDRA':
        print('\033[31mO PC GANHOU')
    else:
        print('OPÇÃO INVÁLIDA')
elif pcesco==t:
    if esco=='TESOURA':
        print('\033[33mDESSA VEZ EMPATAMOS!\033[m')
    elif esco == 'PEDRA':
        print('\033[32mVOCÊ GANHOU!\033[31')
    elif esco == 'PAPEL':
        print('\033[31mO PC GANHOU')
elif esco > 2:
        print('OPÇÃO INVÁLIDA')


