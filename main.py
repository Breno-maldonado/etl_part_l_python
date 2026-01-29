import requests
import numpy as np
import pandas as pd
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
    limit = 10
    while True:
        data = extracao_dados(url + "/" + str(i))
        if data and i <= limit:
            load_data(data, "data/" + endpoint)
        elif i >= limit:
            break
        else:
            print(f"Erro ao extrair dados da API: {data}")
            break
        i += 1

def transform_data_json_to_csv(endpoint, i):
    with open(f"raw/{endpoint}/{i}.json", "r") as file:
        data = json.load(file)
    
    df = pd.DataFrame(data)
    df.to_csv(f"curated/{endpoint}/{i}.csv", index=False)

endpoints = ["user", "products"]

transform_data_json_to_csv("user", 1)