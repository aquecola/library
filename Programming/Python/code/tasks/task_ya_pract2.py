def get_together_games(games_1, games_2):
    games_1 = set(games_1)
    games_2 = set(games_2)
    together_games = games_1.intersection(games_2)
    for game in together_games:
        print("👾", game)

anfisa_games = [
    'Online-chess',
    'Города',
    'DOOM',
    'Крестики-нолики'
]
alisa_games = [
    'DOOM',
    'Online-chess',
    'Города',
    'GTA',
    'World of tanks'
]
get_together_games(anfisa_games, alisa_games)