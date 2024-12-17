def leiaInt(msg):
    while True:
        user_input = input(f'{msg}')
        if user_input.isnumeric():
            return user_input
        else:
            print(f'\033[31mERRO! Digite um número inteiro válido.\033[m')


n = leiaInt('Digite um numero: ')
print(f'\033[32mVocê digitou o número {n}\033[m')