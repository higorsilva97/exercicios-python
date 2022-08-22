dados = {}
gols = 0
listagols = list()
totgols = 0
jogadores = list()
resp = ''
while True:
    dados.clear()
    dados['nome'] = str(input('Nome do jogador: '))
    partidas = int(input('Quantidade de partidas: '))
    dados['partidas'] = partidas
    jogadores.clear()

    for i in range(0, partidas):
        gols = int(input(f'Quantos gols na {i+1} partida: '))
        totgols += gols #sun(partidas)
        listagols.append(gols)
    dados['gols'] = listagols
    dados['totalgols'] = totgols
    jogadores.append(dados.copy())
    resp = str(input('Deseja continuar [S/N]:'))
    if resp in 'Nn':
        break

print('='*30)
print('cod ', end='')
for item in dados.keys():
    print(f'{item:<15}', end='')
print()
for k, v in enumerate(jogadores):
    print(f'{k:>4}', end='')
    for t in v.values():
        print(f'{str(t):<15}', end='')
    print()


print(f'O jogador {dados["nome"]}  jogou {dados["partidas"]} partidas')
for j, g in enumerate(listagols):
    print(f'Na partida {j+1}, marcou {g} gols')
print(f'Foi um total de {totgols}')
print('='*30)

print(jogadores)


