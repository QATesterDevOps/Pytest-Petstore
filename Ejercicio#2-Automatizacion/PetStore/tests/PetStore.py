import requests
import pytest
import allure
from config import Data
from utils import read_file

@allure.title("Registro de una nueva mascota")
def test_new_pet_200() -> None:
    payload = read_file.reader("post.json")
    headers = {
        "Accept":"application/json"
    }
    response = requests.post(Data.BASE_URL + "/v2/pet", json=payload, headers=headers, timeout=10)    
    assert response.status_code == 200

@allure.title("Registro de una nueva mascota con endpoint incorrecto")
def test_new_pet_404() -> None:
    payload = read_file.reader("post.json")
    headers = {
        "Accept":"application/json"
    }
    response = requests.post(Data.BASE_URL + "/v2/petes", json=payload, headers=headers, timeout=10)    
    assert response.status_code == 404

@allure.title("Registro de una nueva mascota con formato de datos incorrectos")
def test_new_pet_500() -> None:
    payload = read_file.reader("post_500.json")
    headers = {
        "Accept":"application/json"
    }
    response = requests.post(Data.BASE_URL + "/v2/pet", json=payload, headers=headers, timeout=10)    
    assert response.status_code == 500

@allure.title("Actualizar informacion de la mascota")
def test_add_object_pet_200() -> None:
    payload =  read_file.reader("put.json")
    headers = {
        "Accept":"application/json"
    }
    response = requests.put(Data.BASE_URL + "/v2/pet", json=payload, headers=headers, timeout=10)    
    assert response.status_code == 200    

@allure.title("Actualizar informacion de la mascota con endpoint incorrecto")
def test_add_object_pet_404() -> None:
    payload =  read_file.reader("put.json")
    headers = {
        "Accept":"application/json"
    }
    response = requests.put(Data.BASE_URL + "/v2/mascota", json=payload, headers=headers, timeout=10)    
    assert response.status_code == 404 

@allure.title("Actualizar informacion de la mascota con formato de datos incorrectos")
def test_add_object_pet_500() -> None:
    payload =  read_file.reader("put_500.json")
    headers = {
        "Accept":"application/json"
    }
    response = requests.put(Data.BASE_URL + "/v2/pet", json=payload, headers=headers, timeout=10)    
    assert response.status_code == 500     

@allure.title("Busqueda de las mascotas por estados")
def test_find_status_200() -> None:
    response = requests.get(Data.BASE_URL + "/v2/pet/findByStatus?status=sold", timeout=10)
    assert response.status_code == 200

@allure.title("Busqueda de las mascotas por estados con endpoint incorrecta")
def test_find_status_404() -> None:
    response = requests.get(Data.BASE_URL + "/v2/pet/findByStatus7?status=sold", timeout=10)
    assert response.status_code == 404    

@allure.title("Busqueda de las mascotas por ID")
def test_find_ID_200() -> None:
    response = requests.get(Data.BASE_URL + "/v2/pet/1245788", timeout=10)
    assert response.status_code == 200

@allure.title("Busqueda de las mascotas por ID con endpoint incorrecta")
def test_find_ID_404() -> None:
    response = requests.get(Data.BASE_URL + "/v2/pet//1245788", timeout=10)
    assert response.status_code == 404      

@allure.title("Eliminacion de las mascotas por ID")
def test_delete_pet_200() -> None:
    response = requests.delete(Data.BASE_URL + "/v2/pet/1245788", timeout=10)
    assert response.status_code == 200

@allure.title("Eliminacion de las mascotas por ID con endpoint incorrecta")
def test_delete_pet_404() -> None:
    response = requests.delete(Data.BASE_URL + "/v2/pet/1245788//", timeout=10)
    assert response.status_code == 404    
