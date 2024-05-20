import os
from random import choices

os.environ['MONGO_USER'] = 'user'
os.environ['MONGO_PASSWORD'] = 'password'
os.environ['MONGO_HOST'] = 'localhost'
os.environ['MONGO_PORT'] = '27017'
os.environ['MONGO_DBNAME'] = 'test_db'
os.environ['MONGO_COLLECTION_FROM'] = 'coll_from'
os.environ['MONGO_COLLECTION_TO'] = 'coll_to'

from pymongo import MongoClient



# mongodb://backend-rc:test11223344@sa56-hapr-2.bank.net:27017/backend-rc?authSource=backend-rc


creds = {
    'user': os.environ['MONGO_USER'],
    'password': os.environ['MONGO_PASSWORD'],
    'host': os.environ['MONGO_HOST'],
    'port': int(os.environ['MONGO_PORT']),
    'db': os.environ['MONGO_DBNAME'],
    'collection_from': os.environ['MONGO_COLLECTION_FROM'],
    'collection_to': os.environ['MONGO_COLLECTION_TO'],
}
client = MongoClient(f'mongodb://{creds['user']}:{creds['password']}@{creds['host']}:{creds['port']}')
db = client[creds['db']]
collection_from = db[creds['collection_from']]
collection_to = db[creds['collection_to']]


# prepare
collection_from.delete_many({})

documents = [{'inn': ''.join(choices('1234567890', k=10))} for _ in range(12)]

collection_from.insert_many(documents)



for doc in collection_from.find({}):
    print(doc)
    # collection_to.update_one(
    #     {
    #         'id': doc['id']
    #     },
    #     {
    #         '$set': {'inn': doc['inn']}
    #     },
    # )





# docs = collection_to.find()
#
# for doc in docs:
#     print(doc)
