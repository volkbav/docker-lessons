from pymongo import MongoClient
from pprint import pprint

MONGO_URL = "mongodb://mongo:27017"  # mongo - имя сервиса в докер
client = MongoClient(MONGO_URL)
db = client.admin  # admin - бд по умолчанию
dbs_list = db.command("listDatabases")
pprint(dbs_list)

print('end')