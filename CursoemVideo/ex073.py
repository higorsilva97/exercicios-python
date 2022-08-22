times = ('Palmeiras', 'Corinthians', 'Athletico-PR', 'Internacional', 'Atlético-MG', 'Fluminense', 'Santos',
	    'São Paulo', 'Flamengo', 'Botafogo', 'Avaí', 'Bragantino',  'Atlético-GO', 'Goiás', 'Ceará', 'Coritiba',
         'América-MG', 'Cuiabá', 'Juventude', 'Fortaleza')
print('Os cinco primeiros')
print(f'Os 5 primeiros : {times[0:5]}')
print(f'Os 4 ultimos: {times[-4:]}')
print(f'Times em ordem alfabética: {sorted(times)}')
print(f'O Santos tá na posição {times.index("Santos")+1}')
