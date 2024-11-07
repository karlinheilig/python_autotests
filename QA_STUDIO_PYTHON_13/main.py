import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'be6ac83f8ff343ed53fc91a5c0e2b5df'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
body_create = {
    "name": "Бульбазаврик3",
    "photo_id": 1
}

body_update = {
    "pokemon_id": "81277",
    "name": "Бубубу2",
    "photo_id": 2
}


body_catch_in_pokeball = {
    "pokemon_id": "81277"
}

response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
message_create = response_create.json()
print(message_create)


response_update_name = requests.put(url = f'{URL}/pokemons',headers = HEADER, json = body_update)
message_update_name = response_update_name.json()
print(message_update_name)


response_catch_in_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_catch_in_pokeball)
message_catch_in_pokeball = response_catch_in_pokeball.json()
print(message_catch_in_pokeball)