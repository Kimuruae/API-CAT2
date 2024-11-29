import requests
BASE_URL = 'http://127.0.0.1:5000/products'

# Add a new product
def add_product(name, description, price):
    response = requests.post(BASE_URL, json={"name": name, "description": description, "price": price})
    print(response.status_code, response.json())

# Retrieve all available products
def get_products():
    response = requests.get(BASE_URL)
    print(response.status_code, response.json())

# Example Usage
add_product("Laptop", "High-performance laptop", 1200.50)
add_product("Smartphone", "Latest model smartphone", 899.99)
get_products()
