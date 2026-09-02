shopping_cart = {
    "apple": 2.5,
    "banana": 1.0,
    "orange": 1.5
}
product = input("Enter the product you want to check: ")
if product in shopping_cart:
    print(shopping_cart[product])
