
from flask import Flask, request, jsonify
from pymongo import MongoClient
from bson import ObjectId
import json

app = Flask(__name__)

# Connect to MongoDB Atlas
client = MongoClient("mongodb+srv://sumansaw81:wYORaUs4v1OWeUMY@cluster0.dipynva.mongodb.net/?retryWrites=true&w=majority")
db = client.get_database('mydatabase')
collection = db['mycollection']


@app.route('/')
def server_check():
    return jsonify({'message':'Hello World!!'})


@app.route('/create', methods=['POST'])
def create():
    data = request.get_json()
    collection.insert_one(data)
    return jsonify({'message': 'Document created successfully'})


@app.route('/read', methods=['GET'])
def read():
    documents = list(collection.find({}, {'_id': 0}))
    return jsonify(documents)


@app.route('/read/<string:id>' , methods=['GET'])
def readByID(id):
    document_id = ObjectId(id)
    user = collection.find_one({'_id': document_id}, {'_id': 0})
    if user:
        return jsonify(user)
    else:
        return jsonify({'message': 'User not found'})


@app.route('/update/<string:id>', methods=['PUT'])
def update(id):
    data = request.get_json()
    document_id = ObjectId(id)
    collection.update_one({'_id': document_id}, {'$set': data})
    return jsonify({'message': 'Document updated successfully'})


@app.route('/delete/<string:id>', methods=['DELETE'])
def delete(id):
    document_id = ObjectId(id)
    collection.delete_one({'_id': document_id})
    return jsonify({'message': 'Document deleted successfully'})


if __name__ == '__main__':
    app.run(debug=True)
