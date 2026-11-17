def register_customer(name):
    print(f"Customer registered: {name}")
    return {"name": name}


def show_products():
    products = {
        "Laptop": 50000,
        "Mobile": 20000,
        "Headphones": 2000,
    }

    print("\nAvailable products:")
    for name, price in products.items():
        print(f"{name}: Rs. {price}")

    return products


def add_to_cart(products, product_name, quantity):
    if product_name not in products:
        raise ValueError(f"Product not found: {product_name}")

    if quantity <= 0:
        raise ValueError("Quantity must be greater than zero")

    item = {
        "product": product_name,
        "price": products[product_name],
        "quantity": quantity,
    }

    print(f"Added to cart: {product_name} x {quantity}")
    return item


def calculate_total(cart):
    return sum(
        item["price"] * item["quantity"]
        for item in cart
    )


def make_payment(customer, amount):
    print("\nProcessing simulated payment...")
    print("Customer:", customer["name"])
    print(f"Total amount: Rs. {amount}")
    print("Payment successful (demo only).")


def main():
    print("=== MINI E-COMMERCE APPLICATION ===")

    customer = register_customer("Veera")
    products = show_products()

    cart = []
    cart.append(add_to_cart(products, "Laptop", 1))
    cart.append(add_to_cart(products, "Headphones", 2))

    total = calculate_total(cart)
    make_payment(customer, total)
main()

#if __name__ == "__main__":
    #main()
#This is called the Main Guard or Entry Point Check in Python.
#__name__ is a special built-in variable in Python
# When you run a Python file directly, Python automatically sets its __name__ value to "__main__"
# main()

# If the condition is True, Python calls the main() function.
    
#If another Python file imports this one, __name__ gets the file’s module name instead, so the condition is false and main() doesn’t run automatically.
