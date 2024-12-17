from random import randint
menor = 9
maior = 0

numeros = (randint(0,9), randint(0,9), randint(0,9), randint(0,9), randint(0,9))
print(numeros)
print(max(numeros))
print(min(numeros))
for numM in numeros:
    if numM < menor:
        menor = numM
    if numM > maior:
        maior = numM
print(f'O menor numero é {menor}.')
print(f'O maior numero é {maior}.')