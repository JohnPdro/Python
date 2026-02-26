from pymongo import MongoClient

client = MongoClient()

mydb = client.obcblog # Data base 
mycol = mydb.posts # Colection

post1 = {
    "title": "Fast API",
    "category": "Back-End",
    "author" : {
        "name": "João",
        "email": "joao@gmail.com"
    }
}

result = mycol.insert_one(post1)
print("Documento incluído com sucesso")