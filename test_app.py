import pytest
from app import app, inventory
import app as app_module


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_get_inventory(client):
    response = client.get("/inventory")

    assert response.status_code == 200
    assert isinstance(response.json, list)


def test_get_item(client):
    response = client.get("/inventory/1")

    assert response.status_code == 200
    assert response.json["product_name"] == "Organic Almond Milk"


def test_add_item(client):
    new_item = {
        "product_name": "Test Product",
        "brands": "Test Brand",
        "ingredients_text": "Test ingredients",
        "price": 2.99,
        "stock": 5,
        "barcode": "987654321"
    }

    response = client.post("/inventory", json=new_item)

    assert response.status_code == 201
    assert response.json["product_name"] == "Test Product"


def test_update_item(client):
    updated_data = {
        "price": 6.99,
        "stock": 30
    }

    response = client.patch("/inventory/1", json=updated_data)

    assert response.status_code == 200
    assert response.json["price"] == 6.99
    assert response.json["stock"] == 30


def test_delete_item(client):
    response = client.delete("/inventory/2")

    assert response.status_code == 200
    assert response.json["message"] == "Item deleted"


def test_search_product(client):
    app_module.find_product = lambda barcode: {
    "barcode": barcode,
    "brands": "Cristaline",
    "product_name": "isabelle",
    "ingredients_text": "Eau de source"
}
    response = client.get("/inventory/search/3274080005003")

    assert response.status_code == 200
    assert response.json["barcode"] == "3274080005003"
    assert response.json["brands"] == "Cristaline"