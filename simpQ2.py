contacts = {
    "Papa": "0242658507",
    "Ken": "0242658508",
    "Ama": "0242658509"
}
number = input("Enter the name of the contact you want to access: ")
if number in contacts:
    print(contacts[number])