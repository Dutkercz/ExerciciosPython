from random import randint
jogos = [0,0,0,0,0,0]
n = int(input('Digite quantos jogos deseja fazer: '))
for c in range (0, n):
    jogos = [[randint(1,60), randint(1,60), randint(1,60), randint(1,60), randint(1,60), randint(1,60)]] * n

    print(f'Os jogos gerados foram: {jogos}')