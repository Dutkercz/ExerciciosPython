list=[[],[], []]
for c in range (1,8):
    n = int(input(f'Digite o {c}º valor: '))
    if n % 2 == 0 and n != 0:
        list[0].append(n)
    elif n % 2 == 1:
        list[1].append(n)
    elif n == 0:
        list[2].append(n)
print(f'Os valores PARES são: {sorted(list[0])}')
print(f'Os valores IMPARES são: {sorted(list[1])}')
if len(list[2])>0:
    print(f'Você digitou o número 0, {len(list[2])} vez(es)')

