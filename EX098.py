from time import sleep

print('Contando de 1 a 10 ...')
for c in range (1, 11):
    print(f'{c}', end=' ')
    sleep(0.5)
print('FIM')

print('Contando de 10 a 1 ...')
for c in range(10, 0, -2):
    print(f'{c}', end=' ')
    sleep(0.5)
print('FIM')

print('AGORA É SUA VEZ...')

ni = int(input('Inicio: '))
nf = int(input('Final: '))
np = int(input('Passo:'))

def contador(i, f, p):
    if i > f:
        if p == 0 :
            print(f'Contando de {i} até {f} de {'1'} em {'1'}')
            p = -1
        elif p > 0:
            print(f'Contando de {i} até {f} de {p} em {p}')
            p*=-1
        elif p < 0:
            print(f'Contando de {i} até {f} de {p*-1} em {p*-1}')
        for c in range(i, f - 1, p):
            print(f'{c}', end=' ')
            sleep(0.5)
    elif i < f:
        if p == 0:
            p = 1
        if p < 0:
            p*=-1
        print(f'Contando de {i} até {f} de {p} em {p}')
        for c in range(i, f + 1, p):
            print(f'{c}', end=' ')
            sleep(0.5)


contador(ni, nf, np)