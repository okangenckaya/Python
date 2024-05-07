
favorite_mortal_kombat_games = {

    'Mortal Kombat Trilogy:': 1996,
    'Mortal kombat 2:': 1992,
    'Mortal Kombat: Armageddon:': 2006,
    'Mortal Kombat Komplete Edition:': 2012,
    'Mortal Kombat X:': 2015,
    'Mortal Kombat 11:': 2019,
    'Mortal Kombat 1 (Rebooted):': 2023,
}

#How to call item of this dictionary?

for key, value in favorite_mortal_kombat_games.items():
    print(key, value)


#How to call only game names?

for key in favorite_mortal_kombat_games.keys():
    print(key)

#How to call only release years ?

for value in favorite_mortal_kombat_games.values():
    print(value)
