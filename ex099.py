from time import sleep

#ROTINAS
def maior(*num):
    print('==-' * 20)
    print('ANALISANDO...')
    print('==-' * 20)
    sleep(0.8)
    print(num, flush=True)
    sleep(0.8)
    if len(num) == 0:
        print('Não foi informado nenhum valor!')
    else:
        print(f'foram informados {len(num)} valor(es)')
        sleep(1)
        print(f'O maior valor informado foi {max(num)}')
        print('==-' * 20)
    sleep(0.8)

#PROGRAMA PRINCIPAL

maior(1, 22, 43, 545.76, 43, 4343, 65653)
maior(1, 5151, 484, 4184, 74, 4844, 8448841)
maior()