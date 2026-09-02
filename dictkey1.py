personal_info = {
    "name" : "John",
    "age" : 30,
    "country" : "Ghana"
}
key = input("Enter the key you want to access: ")
if key in personal_info:
    print(personal_info[key])
else:
    print("Key not found in the dictionary.")