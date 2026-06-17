correct_password = "secure123"
attempts = 0
while True:
    password = input("Enter the password to login: ")
    attempts = attempts + 1
    if password == correct_password:
        break
    else:
        print("Incorrect password. Please try again.")
print("Access Granted!")
print("The number of attempts:", attempts)
        