import requests
import pytest 

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'be6ac83f8ff343ed53fc91a5c0e2b5df'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
TRAINER_ID = '9298'

def test_status_code(): 
     response_trainers = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
     assert response_trainers.status_code == 200

def test_trainer_id():
     response_trainer_id = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
     assert response_trainer_id.json()['data'][0]['id'] == TRAINER_ID