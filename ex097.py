'''def escreva(msg):
    for c in msg:
        print('=', end='')
    print(f'\n{msg:^}')
    for c in msg+4:
        print('=',end='')
    print()'''

def escreva(msg):
    tam  = len(msg) + 4
    print('=' * tam)
    print(f'  {msg:}')
    print('=' * tam)

#PROGRAMA PRINCIPAL

escreva('Olá Mundo')
escreva('Curso em Video de Python')
escreva('CRISTIAN TIAGO DUTKERCZ ROSA E JENIFER CARINE DA SILVA MONTEIRO ROSA')