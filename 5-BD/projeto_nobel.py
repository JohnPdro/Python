import requests
from pymongo import MongoClient

# 1 - Conexão com MongoDB
client = MongoClient()
db = client["nobel"]

headers = {
    "User-Agent": "Mozilla/5.0",
    "Accept": "application/json"
}

# Limpa coleções antes de inserir (evita duplicação)
db["nobelPrizes"].delete_many({})
db["laureates"].delete_many({})

# 2 - Buscar Nobel Prizes
url_prizes = "https://api.nobelprize.org/2.1/nobelPrizes?limit=1000"
response_prizes = requests.get(url_prizes, headers=headers)

data_prizes = response_prizes.json()
db["nobelPrizes"].insert_many(data_prizes.get("nobelPrizes", []))

# 3 - Buscar Laureates
url_laureates = "https://api.nobelprize.org/2.1/laureates?limit=1500"
response_laureates = requests.get(url_laureates, headers=headers)

data_laureates = response_laureates.json()
db["laureates"].insert_many(data_laureates.get("laureates", []))

# 4 - Contagem
len_prizes = db["nobelPrizes"].count_documents({})
len_laureates = db["laureates"].count_documents({})

print("Total Nobel Prizes:", len_prizes)
print("Total Laureates:", len_laureates)