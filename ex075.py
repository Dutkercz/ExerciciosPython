from itertools import count

numeros = (int(input('Digite o 1o numero: ')),int(input('Digite o 2o numero: ')),int(input('Digite o 3o numero: ')),
           int(input('Digite o 4o numero: ')))
print(numeros)
print(f'O numero 9 aparece {numeros.count(9)} vezes')
if 3 in numeros:
    print(f'O numero 3 apareceu pela 1a vez na posição {numeros.index(3)+1}')
else:
    print('Nao foi digitado o numero 3!')

print(f'Os numeros PAR(es) são:', end ='' )
for n in numeros:
    if n % 2 == 0 :
       print(f' {n} ', end='>')
print(' FIM')