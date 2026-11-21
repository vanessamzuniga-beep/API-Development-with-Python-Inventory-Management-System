
import requests

BASE_URL = "http://127.0.0.1:5000/inventory"


def show_menu():
    print("\n=== Inventory Management ===")
    print("1. View inventory")
    print("2. View item details")
    print("3. Add product")
    print("4. Update product")
    print("5. Delete product")
    print("6. Find product on OpenFoodFacts")
    print("7. Exit")


def main():
    while True:
        show_menu()
        choice = input("Choose an option: ")

        try:
            if choice == "1":
                response = requests.get(BASE_URL)
                print(response.json())

            elif choice == "2":
                item_id = input("Enter product ID: ")
                response = requests.get(f"{BASE_URL}/{item_id}")
                print(response.json())

            elif choice == "3":
                data = {
                    "product_name": input("Product name: "),
                    "brands": input("Brand: "),
                    "ingredients_text": input("Ingredients: "),
                    "barcode": input("Barcode: "),
                    "price": float(input("Price: ")),
                    "stock": int(input("Stock: "))
                }
                response = requests.post(BASE_URL, json=data)
                print(response.json())

            elif choice == "4":
                item_id = input("Product ID: ")
                data = {
                    "price": float(input("New price: ")),
                    "stock": int(input("New stock: "))
                }
                response = requests.patch(
                    f"{BASE_URL}/{item_id}", json=data
                )
                print(response.json())

            elif choice == "5":
                item_id = input("Product ID: ")
                response = requests.delete(f"{BASE_URL}/{item_id}")
                print(response.json())

            elif choice == "6":
                barcode = input("Enter product barcode: ")
                response = requests.get(
                    f"{BASE_URL}/search/{barcode}"
                )
                if response.status_code != 200:
                    print(response.json())
                    continue
                
                product = response.json()
                print(product)

                add_product = input("Would you like to add this product to inventory? (yes/no): ")

                if add_product.lower() == "yes":
                    product["price"] = float(input("Enter product price: "))
                    product["stock"] = int(input("Enter stock quantity: "))

                    add_response = requests.post(BASE_URL, json=product)
                    print(add_response.json())

            elif choice == "7":
                print("Goodbye!")
                break

            else:
                print("Invalid choice. Try again.")

        except (requests.RequestException, ValueError) as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    main()
