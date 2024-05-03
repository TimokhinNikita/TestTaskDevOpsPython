import pdb
import cProfile

from flask import Flask, request, jsonify
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://mongodb:27017/keyvalue_db'
mongo = PyMongo(app)

@app.route('/keyvalue', methods=['POST', 'PUT'])
def set_key_value():
    pdb.set_trace()  # Точка остановки
    data = request.get_json()
    key = data.get('key')
    value = data.get('value')
    if not key or not value:
        return jsonify({'error': 'Both key and value are required'}), 400
    mongo.db.keyvalue_collection.update_one({'key': key}, {'$set': {'value': value}}, upsert=True)
    return jsonify({'message': f'Key {key} set to value {value}'}), 200

@app.route('/keyvalue/<key>', methods=['GET'])
def get_key_value(key):
    data = mongo.db.keyvalue_collection.find_one({'key': key})
    if data:
        return jsonify({'key': key, 'value': data['value']}), 200
    else:
        return jsonify({'error': 'Key not found'}), 404

@app.route('/alarm', methods=['POST'])
def handle_memory_alarm():
    data = request.get_json()
    message = data.get('message')
    print("Received memory alarm:", message)
    return jsonify({'message': 'Alarm received and processed'}), 200

if __name__ == '__main__':
    profile_file = 'profile_results.txt'
    cProfile.run('app.run(host="0.0.0.0", port=8080)', filename=profile_file)
