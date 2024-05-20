import os

from pymongo import MongoClient


creds = {
    'user': os.environ['MONGO_USER'],
    'password': os.environ['MONGO_PASSWORD'],
    'host': os.environ['MONGO_HOST'],
    'port': int(os.environ['MONGO_PORT']),
}
client = MongoClient(f'mongodb://{creds['user']}:{creds['password']}@{creds['host']}:{creds['port']}')
db = client[os.environ['MONGO_DBNAME']]
collection_from = db[os.environ['MONGO_COLLECTION_FROM']]
collection_to = db[os.environ['MONGO_COLLECTION_TO']]
prop = os.environ['MONGO_PROP_TO_TRANSFER']
chunk_size = int(os.environ['CHUNK_SIZE'])

def process_chunk(chunk):
    for doc in chunk:
        collection_to.update_one(
            {'_id': doc['_id']},
            {'$set': {prop: doc[prop]}},
        )

cursor = collection_from.find()

chunk = []

for doc in cursor:
    chunk.append(doc)
    if len(chunk) >= chunk_size:
        process_chunk(chunk)
        chunk = []

if chunk:
    process_chunk(chunk)

client.close()
