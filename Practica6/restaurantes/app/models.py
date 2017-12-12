from pymongo import MongoClient

# Create your models here.

client = MongoClient()
db = client.test                #base de datos
restaurantes = db.restaurants   #colección
