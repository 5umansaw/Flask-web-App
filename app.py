
from flask import Flask, request, jsonify
from pymongo import MongoClient
from bson import ObjectId
from userModel import User
import json

app = Flask(__name__)

# Connect to MongoDB Atlas
client = MongoClient("mongodb+srv://sumansaw81:wYORaUs4v1OWeUMY@cluster0.dipynva.mongodb.net/?retryWrites=true&w=majority")
db = client.get_database('mydatabase')
collection = db['mycollection']

user_model = User(db , collection)

@app.route('/')
def server_check():
    return jsonify({'message':'Hello World!!'})


@app.route('/create', methods=['POST'])
def create():
    data = request.get_json()
    user_model.create(data)
    return jsonify({'message': 'Document created successfully'})


@app.route('/read', methods=['GET'])
def read():
    users = user_model.read_all()
    return jsonify(users)


@app.route('/read/<string:id>' , methods=['GET'])
def readByID(id):
    user = user_model.read_by_id(id)
    if user:
        return jsonify(user)
    else:
        return jsonify({'message': 'User not found'})


@app.route('/update/<string:id>', methods=['PUT'])
def update(id):
    data = request.get_json()
    user_model.update(id , data)
    return jsonify({'message': 'Document updated successfully'})


@app.route('/delete/<string:id>', methods=['DELETE'])
def delete(id):
    user_model.delete(id)
    return jsonify({'message': 'Document deleted successfully'})


if __name__ == '__main__':
    app.run(debug=True)
