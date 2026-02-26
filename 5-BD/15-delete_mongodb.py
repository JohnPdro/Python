from pymongo import MongoClient

client = MongoClient()

mydb = client.obcblog # Data base 
mycol = mydb.posts # Colection

myquery = {"category": "Data Analysis"}

x = mycol.delete_one(myquery)

print(f"{x.deleted_count} documento excluído")