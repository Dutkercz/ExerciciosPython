matriz = [[0,0,0], [0,0,0], [0,0,0]]
somapar = soma3c = maior2l = 0
for lis in range (0,3):
    for sublis in range (0,3):
        n = int(input(f'Digite um valor para a posição {lis}x{sublis}: '))
        matriz[lis][sublis]=n
        if n % 2 ==0:
            somapar+= n
print('=='*30)
maior2l = max(matriz[1])
print(f'O maior número da 2ª linha é {maior2l}')
print('=='*30)
for l in range (0,3):
    soma3c += matriz[l][2]
#som3c = matriz[0][2] + matriz[1][2] + matriz[2][2]
print(f'A soma dos números da 3ª coluna é {soma3c}')
print('=='*30)
print(f'A soma dos números PARES da matriz é {somapar}')
print('=='*30)
for l in range (0,3):
    for c in range (0,3):
        print(f'[ {matriz[l][c]:^5} ] ',end='')
    print()