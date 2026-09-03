products = {
    "soda": 10,
    "chips": 5,
    "candy": 2,
    "cookies": 8
}
product_name = input("Enter the product name: ")
if product_name in products:
    print(product_name,"is in stock")
else: 
    print(product_name,"is not in stock")