'''Elabore um programa que calcule o valor a ser pago por um produto,
 considerando o seu preço normal e condição de pagamento:'''

preco=float(input('Digite o valor do produto: R$ '))
pgto=int(input('''Qual a forma de pagamento?
[1] Á vista (dinheiro/pix).
[2] Á vista cartão débito.
[3] Crédito até 2x.
[4] Crédito 3x ou mais.
Opção: '''))

print('O preço formal do produto é \033[33mR$ {:.2f}\033[m.'.format(preco), end='\n')
if pgto == 1:
    preco = preco*0.90
    print ('Para pagamentos em DINHEIRO ou PIX há 10% de desconto.\nO preço final será \033[32mR$ {:.2f}\033[m'.format(preco))
elif pgto == 2:
    preco = preco*0.95
    print('Para pagamentos no DÉBITO há 5% de desconto.\nO preço final será \033[32mR$ {:.2f}\033[m'.format(preco))
elif pgto == 3:
    print('Para pagamentos em até 2x no CRÉDITO, o valor se mantém o mesmo.\nTotal \033[32mR$ {:.2f}\033[m.'.format(preco))
elif pgto == 4:
    vezes=int(input('''Em quantas vezes gostaria de dividir?
     / '''))
    preco = preco*1.2
    precoD = preco/vezes
    print('Para pagamentos no CRÉDITO em 3x ou mais há 20% de acréscimo.\nO preço final será \033[32mR$ {:.2f}\033[m'.format(preco))
    print('E será dividido em \033[34m{}X de R$ {:.2f}\033[m'.format(vezes, precoD))
else:
    print('OPÇÃO INVÁLIDA!')
