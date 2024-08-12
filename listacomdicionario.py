game = {}
games = []

for i in range(3):
    game['nome'] = input('Qual o nome do jogo? ')
    game['videogame'] = input('Para qual video game ele foi lançado? ')
    game['ano'] = input('Qual o ano de lançamento? ')
    games.append(game.copy())
print('-' * 20)
for jogos in games:
    for chave, valor in jogos.items():
        print(f'O campo {chave} tem o valor {valor}.')



games =  {'nome' : [], 'videogame' : [], 'ano' : []}
for i in range (3):
    nome = input('Qual o nome do jogo? ')
    videogame = input('Para qual video game ele foi lançado? ')
    ano = input('Qual o ano de lançamento? ')
    games['nome'].append(nome)
    games['videogame'].append(videogame)
    games['ano'].insert(ano)
print('-' * 20)
print(games)