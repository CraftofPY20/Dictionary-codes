capitals = {
    "Ghana" : "Accra",
    "Nigeria" : "Abuja",
    "Kenya" : "Nairobi",
    "South Africa" : "Pretoria"
}
country = input("Enter the country name: ")
if country in capitals:
    print( capitals[country])
else:
    print("Country not found in the dictionary.")