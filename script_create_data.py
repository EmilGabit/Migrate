import json
from pymongo import MongoClient

from db.data import chats_collection

client = MongoClient('mongodb://localhost:27017/')
db = client.grinatomtg  # Название db
chats_collection = db.chats# коллекция для ранения чатов


with open('output.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
#
# Вставьте данные в коллекцию
if isinstance(data, list):
    chats_collection.insert_many(data)  # Используйте insert_many для списка документов
else:
    chats_collection.insert_one(data)    # Используйте insert_one для одиночного документа

print('Данные записаны')