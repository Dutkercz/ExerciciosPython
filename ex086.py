matriz = [[0,0,0], [0,0,0], [0,0,0]]
for lis in range (0,3):
    for sublis in range (0,3):
        n = int(input(f'Digite um valor para a posição {lis}x{sublis}: '))
        matriz[lis][sublis]=n
print('=='*30)
for l in range (0,3):
    for c in range (0,3):
        print(f'[ {matriz[l][c]:^5} ] ',end='')
    print() # esse print quebra o laço do end=  da linha de cima.