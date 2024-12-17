'''Escreva um programapara aprovar o empréstimo bancário
para a compra de uma casa.Pergunte o valor da casa, o salário do comprador e em quantos
a nos ele vai pagar.A prestação mensal não pode exceder 30 % do salário ou então o empréstimo será negado.'''
print('-=-'*19)
print('            \033[7mCalculadora de Financiamento\033[m ')
print('-=-'*19)

n=str(input('Digite o seu nome completo: ')).strip().title()
valor=float(input('Qual o valor do imóvel: R$ '))
renda=float(input('Qual a sua renda mensal: R$ '))
ren2=str(input('Deseja adicicionar mais alguma renda?\n (1 - sim) ou (2 - não) :'))
if ren2=='1':
    renda2=float(input('Digite o valor da renda completamentar: R$ '))
    renda = renda + renda2
anos=int(input('Em quantos anos quer dividir? '))
parcela= valor / (anos*12)
print(renda)
parmax= renda*0.30

if parcela <= parmax :
    print('                 \033[32mAPROVADO!\033[m')
    print('Para um financiamento de R$ {}, em {} vezes, tera uma parcela de {}'.format(valor, (anos*12), parcela))
    print('Com a sua renda mensal de R$ {}, a parcela maxima deve ser R$ {}'.format(renda,parmax))
else:
    print('Infelizmente \033[31mnão conseguimos aprovar\033[m seu financiamento!')
    print('Com a sua renda mensal de R$ {}, a parcela maxima deve ser R$ {}'.format(renda, parmax))

