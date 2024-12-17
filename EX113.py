def leiaInt(msg):
    while True:
        try:
            user_input = int(input(f'{msg}'))
        except (ValueError, TypeError, KeyboardInterrupt):
            print(f'\033[31mERRO! você não digitou um numero INTEIRO\033[m')
            continue
        else:
            return user_input



def leiaFloat(msg):
    while True:
        try:
            user_input = float(input('Digite um número REAL: '))
        except (TypeError, ValueError, KeyboardInterrupt):
            print(f'\033[31mERRO. Por favor digite um número REAL.\033[m')
            continue
        else:
            return user_input


int = leiaInt('Digite um nÚmero Inteiro: ')
real = leiaFloat('Digite um nÚmero REAL: ')
print(int, real)
