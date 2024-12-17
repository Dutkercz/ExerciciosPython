def criarArq(nome):
    a = open(nome, 'wt+')
    a.close()


def arqEx(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def leiaInt(msg):
    while True:
        try:
            user_input = int(input(f'{msg}'))
        except (ValueError, TypeError, KeyboardInterrupt):
            print(f'\033[31mERRO! você não digitou um numero INTEIRO\033[m')
            continue
        else:
            return user_input


def linha(tam = 42):
    return '=' * tam


def cabecalho (msg):
    print(linha())
    print(msg.center(42))
    print(linha())


def menu(listaOp):
    cabecalho('MENU PRICIPAL')
    for i, v in enumerate(listaOp):
        print(f'\033[32m{i+1}\033[m > \033[34m{v}\033[m ')
    print(linha())
    opc = leiaInt('Digite a opção desejada: ')
    return opc


def lerArq(arquivo):
    try:
       a = open(arquivo, 'rt')
    except:
        print('Erro ao abrir arquivo')
    else:
       cabecalho('\033[32mPESSOAS CADASTRADAS\033[m')
       for l in a:
           dado = l.split(';')
           print(f'{dado[0]} {dado[1]}')
    finally:
        a.close()

def cadPes(arquivo, n = 'Desconhecido', i = 0):
    a = open(arquivo, 'at')
    try:
        a.write(f'{n};{i}')
    except:
        print('HOUVE UM ERRO')
    else:
        print(f'{n} cadastrado')
        a.close()



#PROGRAMA PRINCIPAL
arq = 'cev.txt'
if arqEx(arq):
    print('\033[33mArquivo encontrado\033[m')
else:
    print('\033[31mArquivo não encontrado\033[m')
    criarArq(arq)
    print(f'\033[32mARQUIVO {arq} CRIADO.\033[m')
cabecalho('MENU DE OPÇÕES')
while True:
    resp = menu(['PESSOAS CADASTRADAS', 'CADASTRAR PESSOAS', 'SAIR'])
    if resp == 1:
        lerArq(arq)
    elif resp == 2:
        cabecalho('CADASTRO DE PESSOAS')
        nome = str(input('Nome:')).title().strip()
        idade = leiaInt('Idade: ')
        cadPes(arq, nome, idade)
    elif resp == 3:
        break
    else:
        print('ERRO: escolha uma opção valida')