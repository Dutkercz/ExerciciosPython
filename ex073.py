times = ('Botafogo','Palmeiras', 'Fortaleza','Internacional','Flamengo','São Paulo', 'Cruzeiro','Bahia','Vasco',
'Corinthians','Atlético-MG','Grêmio','Vitória','Fluminense','Criciúma','Juventude','Bragantino','Athletico-PR',
'Cuiabá','Atlético-GO ')

print(f'Os times do Brasileiro sao {times}')
print()
print(f'Sua ordem alfabetica é {sorted(times)}')
print()
print(f'Os 4 ultimos sao {times[-4:]}')
print()
print(f'Os 5 primeiros sao {times[0:5]}')
print()
print(f'O Grêmio esta na {times.index('Grêmio')+1}a posição.')
