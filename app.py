from flask import Flask, request, jsonify
import requests
app = Flask(__name__)

inventory = [
    {"id": 1, "name": "Milk", "price": 120, "stock": 10},
    {"id": 2, "name": "Bread", "price": 60, "stock": 20}
]




@app.route('/')
def home():
    return "Inventory API is running! "

@app.route('/inventory')
def get_inventory():
    return inventory

@app.route('/inventory/<int:item_id>', methods=['GET'])
def get_item(item_id):
    for item in inventory:
        if item['id'] == item_id:
            return item
    return {"error": "Item not found"}, 404

@app.route('/inventory', methods=['POST'])
def add_item():
    new_item = request.get_json()
    inventory.append(new_item)
    return {"message": "Item added successfully"}


@app.route('/inventory/<int:item_id>', methods=['PATCH'])
def update_item(item_id):
    for item in inventory:
        if item["id"] == item_id:
            data = request.json
            item.update(data)
            return jsonify({"message": "Item updated successfully"})
    return jsonify({"error": "Item not found"})


@app.route('/inventory/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    for item in inventory:
        if item["id"] == item_id:
            inventory.remove(item)
            return jsonify({"message": "Item deleted successfully"})
    return jsonify({"error": "Item not found"})

@app.route('/product/<barcode>', methods=['GET'])
def get_product(barcode):
    url = f"https://world.openfoodfacts.org/api/v0/product/{barcode}.json"
    response = requests.get(url)

    if response.status_code == 200:
        return jsonify(response.json())

    return jsonify({"error": "Unable to fetch product"})
if __name__ == '__main__':
    app.run(debug=True)