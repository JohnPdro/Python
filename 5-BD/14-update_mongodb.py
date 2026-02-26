from pymongo import MongoClient
from pprint import pprint

client = MongoClient()

mydb = client.obcblog # Data base 
mycol = mydb.posts # Colection

old_value = {"category": "Data Analysis"}
new_value = {"$set": {"category": "Backend"}}

mycol.update_one(old_value, new_value)

for x in mycol.find() :
    pprint(x)