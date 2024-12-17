'''TRATAMENTO DE ERROS'''

try: #tentar dividir UM MESMO TRY PODE TER VARIOS PROBLEMA
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except: # se der errado faz o passo dentro do except << OBRIGATORIO SE TIVER UM TRY
    print('TIVEMOS UM PROBLEMA')
else: # se der certo faz o passo dentro do else: ATENÇÃO O ELSE é OPCIONAL
    print(f'O resultado é {r}')
finally: #vai executar se der certo ou errado. ATENÇÃO ESSE TAMBEM É OPCIONAL
    print('Volte sempre')