# Inventory Management System


## Introduction
A Python inventory management system built with Flask. This project provides a REST API and command-line interface (CLI) for managing inventory, including adding, viewing, updating, and deleting products. It also integrates with the Open Food Facts API to look up product information using barcodes.


## Features
- View all inventory items
- Retrieve an individual product by ID
- Add new products to inventory
- Update existing product information
- Delete products from inventory
- Search for product information using a barcode through the Open Food Facts API
- Add products found through the external API directly to inventory
- Automated API tests using pytest


## Technology Used
- Python
- Flask
- Requests
- pytest
- Open Food Facts API


## Installation
1) Clone the repository:

   ```bash
   git clone git@github.com:vanessamzuniga-beep/API-Development-with-Python-Inventory-Management-System.git
   ```

2) Navigate into the project folder:

   ```bash
   cd API-Development-with-Python-Inventory-Management-System
   ```

3) Install the project dependencies:

   ```bash
   pipenv install
   ```

4) Install the development dependencies:

   ```bash
   pipenv install --dev
   ```

5) Activate the virtual environment:

   ```bash
   pipenv shell
   ```


## Running the Application
Start the Flask API:

```bash
python app.py
```

The API will run locally at:

`http://127.0.0.1:5000`

In a separate terminal, run the command-line interface:

```bash
python cli.py
```

Follow the menu prompts to manage inventory or search for products.

## API Endpoints
| Method | Endpoint | Description |
|---|---|---|
| GET | `/inventory` | Retrieve all inventory items |
| GET | `/inventory/<item_id>` | Retrieve a product by ID |
| POST | `/inventory` | Add a new product |
| PATCH | `/inventory/<item_id>` | Update an existing product |
| DELETE | `/inventory/<item_id>` | Delete a product |
| GET | `/inventory/search/<barcode>` | Search Open Food Facts for a product |


### Example
Send a POST request to `/inventory` with a JSON body:

```json
{
  "product_name": "Organic Almond Milk",
  "brands": "Silk",
  "ingredients_text": "Water, almonds",
  "price": 4.99,
  "stock": 20,
  "barcode": "123456789"
}
```


## Running Tests
The project uses pytest to test the Flask API endpoints.

Run the test suite with:

```bash
python -m pytest
```

The tests cover retrieving inventory, retrieving individual products, adding products, updating products, deleting products, and searching for products through the external API.


## External API Integration
This project uses the Open Food Facts API to retrieve product information using a barcode. Users can search for products through the CLI and choose to add the retrieved product information to their inventory.

API documentation: https://openfoodfacts.github.io/openfoodfacts-server/api/


## Data Storage
Inventory data is stored in an in-memory Python list. Changes to inventory are temporary and reset when the Flask application restarts.


## Author
Developed as a Python API development project.