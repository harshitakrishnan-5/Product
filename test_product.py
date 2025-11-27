from product import get_product_info

def test_get_product_info():
    expected = "Product ID: L101\nName: Laptop\nQuantity: 5\nPrice: 50000"
    assert get_product_info("L101", "Laptop", 5, 50000) == expected
