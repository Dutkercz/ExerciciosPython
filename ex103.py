from unicodedata import numeric


def ficha(n ='', g = '0'):
    if g.isnumeric():
        gg = int(g)
    else:
        gg = 0
    if not n:
        n = '<Desconhecido>'
    return print(f'O Jogador {n}, marcou {gg} gol(s) no campeonato.')



nome = str(input('Digite o nome do Jogador: ')).strip().title()
gols = input('Gols marcados: ')

ficha(nome, gols)