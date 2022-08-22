def ficha(j='desconhecido', g=0):
    print(f'O jogador {j} fez {g} gols no campeonato!')


jogador = str(input('Nome do jogador: '))
gols = str(input('Numero de gols: '))
if gols.isnumeric():
    g = int(gols)
else:
    g = 0
if jogador.strip() == '':
    ficha(g=gols)
else:
    ficha(jogador, gols)