def leiaDin (txt=''):
    cont = False
    while not cont:
        ler_valor = input(txt).replace(',', '.').strip()
        if ler_valor.isalpha() or ler_valor == '':
            print(f' {ler_valor} é INVÁLIDO')
        else:
            cont = True
            return float(ler_valor)




p = leiaDin('Digite um valor R$: ')
print(f'Você digitou {p}')