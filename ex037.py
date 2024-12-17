num=int(input('Digite um numero inteiro: '))
print('Escolha a base de conversão:')
escolha=str(input('[1]Hexadecimal\n[2]Octal\n[3]Binario\n-> '))
if escolha == '1':
    print('O numero {} em Hexadecimal é {}'.format(num, (hex(num)[2:])))
elif escolha == '2':
    print('O numero {} em Octal é {}'.format(num, (oct(num)[2:])))
elif escolha == '3':
    print('O numero {} em Binário é {}'.format(num, (bin(num)[2:])))
else:
    print('OPÇÃO INVÁLIDA !')