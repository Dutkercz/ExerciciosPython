print('-=-'*18)
print('               Média Bimestral')
print('-=-'*18)

n1=float(input('Nota da primeira prova: '))
n2=float(input('Nota da segunda prova: '))
media = (n1+n2)/2
if media >= 7:
    print('\033[32mAPROVADO!\033[m Sua média foi {:.2f}, Parabéns!'.format(media))
elif media <7 and media >=5 :
    print('\033[33mRECUPERÇÃO!\033[m Sua média foi {:.2f}, estude mais!'.format(media))
elif media < 5:
    print('\033[31mREPROVADO!\033[m Sua média foi {:.2f}, nos vemos no proximo bimestre!'.format(media))
