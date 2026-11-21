from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

inventory = [
    {
        "id": 1,
        "product_name": "Organic Almond Milk",
        "brands": "Silk",
        "ingredients_text": "Filtered water, almonds, cane sugar",
        "price": 4.99,
        "stock": 20,
        "barcode": "123456789"
    },
    {
        "id": 2,
        "product_name": "Cheerios",
        "brands": "General Mills",
        "ingredients_text": "Whole grain oats",
        "price": 5.49,
        "stock": 15,
        "barcode": "016000275"
    }
]


@app.route("/inventory", methods=["GET"])
def get_inventory():
    return jsonify(inventory)


@app.route("/inventory/<int:item_id>", methods=["GET"])
def get_item(item_id):
    for item in inventory:
        if item["id"] == item_id:
            return jsonify(item)
    return jsonify({"error": "Item not found"}), 404


@app.route("/inventory", methods=["POST"])
def add_item():
    data = request.get_json()

    new_item = {
        "id": max([item["id"] for item in inventory], default=0) + 1,
        "product_name": data["product_name"],
        "brands": data.get("brands", ""),
        "ingredients_text": data.get("ingredients_text", ""),
        "price": data["price"],
        "stock": data["stock"],
        "barcode": data.get("barcode", "")
    }

    inventory.append(new_item)
    return jsonify(new_item), 201


@app.route("/inventory/<int:item_id>", methods=["PATCH"])
def update_item(item_id):
    for item in inventory:
        if item["id"] == item_id:
            data = request.get_json()
            item.update(data)
            return jsonify(item)
    return jsonify({"error": "Item not found"}), 404


@app.route("/inventory/<int:item_id>", methods=["DELETE"])
def delete_item(item_id):
    for item in inventory:
        if item["id"] == item_id:
            inventory.remove(item)
            return jsonify({"message": "Item deleted"})
    return jsonify({"error": "Item not found"}), 404


def find_product(barcode):
    url = f"https://world.openfoodfacts.net/api/v3.6/product/{barcode}.json"

    try:
        response = requests.get(
            url,
            auth=("off", "off"),
            timeout=10
        )
        response.raise_for_status()

        data = response.json()

        if data.get("product"):
            return data["product"]

        return None

    except requests.RequestException:
        return None


@app.route("/inventory/search/<barcode>", methods=["GET"])
def search_product(barcode):
    product = find_product(barcode)

    if product is None:
        return jsonify({"error": "Product not found or API unavailable"}), 404

    return jsonify({
        "product_name": product.get("product_name", ""),
        "brands": product.get("brands", ""),
        "ingredients_text": product.get("ingredients_text", ""),
        "barcode": barcode
    })
    

if __name__ == "__main__":
    app.run(debug=True)