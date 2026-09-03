login_credentials = {
    "Jane": "jane@123",
    "Papa": "papa@123",
    "Ama": "ama@123"
}
username = input("Enter your username: ")
password= input ("Enter your password: ")
if username in login_credentials and login_credentials[username] == password:
    print("Login successful!")
else:
    print("Invalid username or password.")