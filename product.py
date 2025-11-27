import sys

def get_product_info(pid, name, qty, price):
    return f"Product ID: {pid}\nName: {name}\nQuantity: {qty}\nPrice: {price}"

if __name__ == "__main__":
    if len(sys.argv) == 5:
        pid, name, qty, price = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
    else:
        pid = input("Enter Product ID: ")
        name = input("Enter Product Name: ")
        qty = input("Enter Quantity: ")
        price = input("Enter Price: ")

    print(get_product_info(pid, name, qty, price))
