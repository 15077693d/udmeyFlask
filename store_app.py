from flask import Flask, request

app = Flask(__name__)

# POST - used to receive data
# GET - used to send data back only

# end point
# POST /store data: {name:}  -> create new store with given name
# GET /store/<string: name>  -> get store resource with given name
# GET /store                 -> get storeList
# POST /store/<string:name>/item data:{name:, price}-> create item in the store with given name
# GET /store/<string:name>/item  -> get the item in the store

"""
Store example:
= 
{
"Mary Store'":{ "name": "Mary Store:
                "items":{
                            "apple":{"name":"apple","price":"100","quantity":"1"}
                                            .
                                            .
                                            .
                        }
                }
                .
                .
                .
}
"""
data = {}


# POST /store data: {name:}  -> create new store with given name
# GET /store                 -> get storeList
@app.route('/store', methods=['GET', 'POST'])
def store_request():
    if request.method == "GET":
        return data
    elif request.method == "POST":
        store_name = request.get_json(silent=True)['name']
        if store_name not in data:
            data[store_name] = {'name': store_name, 'items': {}}
        else:
            return {'error': f'store<{store_name}> exist'}

        return data


# no space between string:store_name
# GET /store/<string:store_name>  -> get store resource with given name
# store_name as arg of method
@app.route('/store/<string:store_name>', methods=['GET'])
def the_store_request(store_name):
    if request.method == "GET":
        if store_name not in data:
            return {'error': f'store<{store_name}> does not exist'}
        return data[store_name]


# POST /store/<string:store_name>/item data:{name:, price}-> create item in the store with given name
# GET /store/<string:store_name>/item  -> get the item in the store
@app.route('/store/<string:store_name>/item', methods=['GET', 'POST'])
def item_request(store_name):
    if request.method == "GET":
        if store_name in data:
            return data[store_name]['items']
        else:
            return {'error': f'store<{store_name}> does not exist'}
    elif request.method == "POST":
        item = request.get_json(silent=True)
        item_name = item['name']
        if store_name in data:
            items = data[store_name]['items']
            if item_name in items:
                return {'error': f'item<{item_name}> exist'}
            else:
                items[item_name] = item
                return data[store_name]['items']
        else:
            return {'error': f'store<{store_name}> does not exist'}


if __name__ == '__main__':
    app.run()
