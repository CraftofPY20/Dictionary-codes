products = {
    "soda": 10,
    "chips": 5,
    "candy": 2,
    "cookies": 8
}
new_product = input("Enter the new product name: ")
new_product_quantity = int(input("Enter the quantity of the new product: "))
products.update({new_product: new_product_quantity})

print(products)
