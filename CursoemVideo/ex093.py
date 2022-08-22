dados = {}
gols = 0
listagols = list()
totgols = 0

dados['nome'] = str(input('Nome do jogador: '))
partidas = int(input('Quantidade de partidas: '))
dados['partidas'] = partidas

for i in range(0, partidas):
    gols = int(input(f'Quantos gols na {i+1} partida: '))
    totgols += gols #sun(partidas)
    listagols.append(gols)

dados['gols'] = listagols
dados['totalgols'] = totgols
print('='*30)
print(dados)
print('='*30)
for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}')

print('='*30)

print(f'O jogador {dados["nome"]}  jogou {dados["partidas"]} partidas')
for j, g in enumerate(listagols):
    print(f'Na partida {j+1}, marcou {g} gols')
print(f'Foi um total de {totgols}')
print('='*30)


