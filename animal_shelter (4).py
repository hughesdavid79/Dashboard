import pymongo
from pymongo.errors import ConnectionFailure, OperationFailure

class AnimalShelter(object):
    def __init__(self, username, password, host, port, db, collection):
        try:
            self.client = pymongo.MongoClient(
                f"mongodb://{username}:{password}@{host}:{port}/{db}?authSource=admin"
            )
            self.database = self.client[db]
            self.collection = self.database[collection]
        except (ConnectionFailure, OperationFailure) as e:
            print(f"Could not connect to MongoDB: {e}")
            self.client = None
            self.database = None
            self.collection = None

    def create(self, data):
        if self.collection is not None and data:
            return self.collection.insert_one(data)
        else:
            raise Exception("Nothing to save, because data parameter is empty or collection is None")

    def read(self, query):
        if self.collection is not None:
            return list(self.collection.find(query))
        else:
            return []

    def update(self, query, data):
        if self.collection is not None:
            return self.collection.update_one(query, {"$set": data})
        else:
            return None

    def delete(self, query):
        if self.collection is not None:
            return self.collection.delete_one(query)
        else:
            return None
