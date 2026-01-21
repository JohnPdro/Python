import pprint

gamesDict = {
    'Resident Evil 4': {
        'yearLaunch': 2023,
        'classificarion': 9.8,
        'genero': ["ação", "aventura"]
    },
    'Mario Odyssey': {
        'yearLaunch': 2017,
        'classification': 10.0,
        'genero': ["aventura", '3d']
    },
    'Donkey Kong Country': {
        'yearLaunch': 1996,
        'classification': 9.5,
        'genero': ["aventura", 'plataforma']
    }
}

pp = pprint.PrettyPrinter(depth=4)
pp.pprint(gamesDict)

# 1 - Buscar informação dentro de um dicionário aninhado
print(gamesDict['Mario Odyssey']['genero'])

# 2 - Adicionar novo item
gamesDict['Mario Odyssey']['players'] = 1
print(gamesDict['Mario Odyssey'])

# 3 - Excluir um dicionário
del gamesDict['Resident Evil 4']
pp.pprint(gamesDict)