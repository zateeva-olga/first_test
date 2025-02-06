#first test

import requests
import pytest

@pytest.fixture()
def obj_id():
    jsonData = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }
    response = requests.post('https://api.restful-api.dev/objects', json=jsonData).json()
    yield response['id']
    requests.delete(f'https://api.restful-api.dev/objects/{response['id']}')

def testCreatePost():
    jsonData = {
    "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }
    response = requests.post('https://api.restful-api.dev/objects', json=jsonData).json()
    print(len(response))
    print(response['id'])
    assert response['name'] == jsonData['name']


def testReadGet(obj_id):
    response = requests.get(f'https://api.restful-api.dev/objects/{obj_id}').json()
    print(response)
    assert response['id'] == obj_id

def testUpdatePUT(obj_id):
    jsonData = {
        "name": "Apple MacBook Pro 17",
        "data": {
            "year": 2020,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }
    response = requests.put(f'https://api.restful-api.dev/objects/{obj_id}', json=jsonData).json()
    print(response)
    assert response['name'] == jsonData['name']

def testDelDelete(obj_id):
    response = requests.delete(f'https://api.restful-api.dev/objects/{obj_id}')
    assert response.status_code ==200
    response = requests.get(f'https://api.restful-api.dev/objects/{obj_id}')
    assert response.status_code == 404
    print(response)

