products = {
    "soap" : 2.5,
    "shampoo" : 5.0,
    "toothpaste" : 3.0
}
product = input("Enter the product name: ")
if product in products:
    print(products[product])
else: 
    print("Product not found in the dictionary.") 