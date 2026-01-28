import requests

import json

def extracao_dados(endpoint):
    print(endpoint)
    response = requests.get(endpoint)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Erro ao extrair dados da API: {response.status_code}")
        return None
    
def load_data(data, path):
    id = data["id"]
    with open(f"{path}/{id}.json", "w") as file:
        json.dump(data, file)

def loop_load_data(endpoint):
    url = "https://dummyjson.com/" + endpoint
    i = 1
    while True:
        data = extracao_dados(url + "/" + str(i))
        if data and i <= 10:
            load_data(data, "data/" + endpoint)
        else:
            print(f"Erro ao extrair dados da API: {data}")
            break
        i += 1

endpoints = ["user", "products"]

for endpoint in endpoints:
    loop_load_data(endpoint)