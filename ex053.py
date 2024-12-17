print('DETECTOR DE PALINDROMO!')
frase = input('Digite uma frase: ').strip().upper()
frase = frase.split()
junto = ''.join(frase)
inverso = ''
for c in range (len(junto)-1 , -1, -1):
    inverso += (junto[c])
print('O inverso de {} é {}'.format((junto' '.join), inverso))
if junto == inverso:
    print('TEMOS UM PALÍNDROMO!')
else:
    print('NÃO TEMOS UM PALÍNDROMO!')
