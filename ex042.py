

s1=float(input('Digite o valor da 1a reta: '))
s2=float(input('Digite o valor da 2a reta: '))
s3=float(input('Digite o valor da 3a reta: '))

if s1 < s2+s3 and s2 < s1+s3 and s3 < s1+s2:
    print('É um triangulo', end=' ')
    if s1==s2 and s2==s3 or s1==s2==s3:
         print('E ele é EQUILATERO')
    elif s1==s2 or s2==s3 or s3==s1:
         print('E ele é ISÓCELES')
    elif s1 != s2 and s2 != s3 and s1 != s3:
         print('E ele é ESCALENO')
else:
    print('Com os segmentos de reta {}, {} e {}, não podemos formar um triangulo.'.format(s1, s2, s3))