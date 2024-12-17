cont = 0
soma = 0
num = int(input('Digite um numero para verificar se ele é primo: '))
for c in range (1, num+1):
    if num % c == 0:
        print('\033[32m{} \033[m'.format(c), end='')
        cont = cont + 1
    else:
        print('\033[31m{} \033[m'.format(c), end='')
if cont == 2:
    print('\nO numero {} é PRIMO'.format(num))
else:
    print('\nO numero {} NÃO é PRIMO'.format(num))
