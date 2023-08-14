from pymongo import MongoClient
from bson import ObjectId

class User:
    def __init__(self, db, collection):
        self.db = db
        self.collection = collection

    def create(self, data):
        self.collection.insert_one(data)

    def read_all(self):
        users = list(self.collection.find({}, {'_id': 0}))
        return users

    def read_by_id(self, id):
        user = self.collection.find_one({'_id': ObjectId(id)}, {'_id': 0})
        return user

    def update(self, id, data):
        self.collection.update_one({'_id': ObjectId(id)}, {'$set': data})

    def delete(self, id):
        self.collection.delete_one({'_id': ObjectId(id)})
