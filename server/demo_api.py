from flask import Flask, abort, jsonify, request

app = Flask(__name__)

# In-memory list of items
items = [
    {'id': 1, 'name': 'Item 1', 'description': 'This is item 1'},
    {'id': 2, 'name': 'Item 2', 'description': 'This is item 2'}
]

# Get all items
@app.route("/items", methods=['GET'])
def get_items():
    return jsonify(items)

# Get a item
@app.route("/items/<int:item_id>", methods=['GET'])
def get_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if item is None:
        abort(404)
    return jsonify(item)

# Creates a new item
@app.route("/items", methods=['POST'])
def create_item():
    if not request.json or not 'name' in request.json:
        abort(400)
    new_item = {
        'id': items[-1]['id'] + 1 if items else 1,
        'name': request.json['name'],
        'description': request.json.get('description', '')
    }
    items.append(new_item)
    return jsonify(new_item), 201


# Updates an existing item
@app.route("/items/<int:item_id>", methods=['PUT'])
def update_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if item is None:
        abort(404)
    if not request.json:
        abort(400)
    item['name'] = request.json.get('name', item['name'])
    item['description'] = request.json.get('description', item['description'])
    return jsonify(item)

# Deletes an item
@app.route("/items/<int:item_id>", methods=['DELETE'])
def delete_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if item is None:
        abort(404)
    items.remove(item)
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)