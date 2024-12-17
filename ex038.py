print('Escreva 2 numeros para compara-los')
n1=float(input('Escreva o 1o número: '))
n2=float(input('Escreva o 2o número: '))
lis=[n1, n2]
print(max(lis))
if n1>n2:
    print('O PRIMEIRO número é maior!')
elif n2>n1:
    print('O SEGUNDO número é maior!')
else:
    print('Os 2 números são IGUAIS!')
