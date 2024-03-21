from flask import Flask, request, jsonify, Response, make_response
from pymongo import MongoClient, ASCENDING
from os import environ
from datetime import datetime
from sys import stderr

app = Flask(__name__)

def startup():
    global collection
    try:
        try:
            client = MongoClient(host=environ['MONGO_HOST'], port=int(environ['MONGO_PORT']), 
                                username=environ['MONGO_USERNAME'], password=environ['MONGO_PASSWORD'])
            db = client['database']
        except Exception as e:
            print(e)
        
        try:
            collection = db.estimate_restock_quantity
            print(collection)
        except:
            print('collection = mydb.estimate_restock_quantity')
        
        try: 
            print(db.list_collection_names())
        except Exception as e:
            print(e)

        # try: 
        #     collection.create_index([('id', ASCENDING)], unique=True)
        #     print('create_index dones')
        # except Exception as e:
        #     print(e)

    except:
        print('='*50)
        print('someting went wrong')
        print('='*50)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/api/estimate/update', methods=['POST'])
def post_estimate():
    params = request.get_json(silent=True)
    
    if not params.get('result'):
        return Response(status=409)

    data = params['result']
    
    if not data:
        return Response(status=400)
    
    # if not data.get('product_id') or not data.get('sku') or not data.get('order_qty'):
    #     return Response(status=409)
    
    if params.get('reset_collection'):
        collection.delete_many({})   
    
    try:
        collection.insert_many(data)
        print('test')
    except:
        return Response(status=409)

    return make_response(jsonify({'message': 'Data inserted'}), 201)

@app.route('/api/estimate/all', methods=['GET'])
def get_estimate():
    l = [{k: v for k, v in c.items() if k != '_id'} for c in collection.find()]
    return jsonify(l)

@app.route('/api/estimate/get/<product_id>', methods=['GET'])
def get_estimate_by_product(product_id):
    l = [{k: v for k, v in c.items() if k != '_id'} for c in collection.find({'product_id': int(product_id)})]
    print(*l, '\n', sep='\n', file=stderr)
    return jsonify(l)

def main():
    startup()
    app.run(host=environ['FLASK_HOST'], port=int(environ['FLASK_PORT']), debug=True)


if __name__ == '__main__':
    main()
