check_password = input("Enter your password: ")

password_length = len(check_password)

if password_length < 1:
    print("Invalid password")

elif password_length < 6:
    print("Weak password")

elif password_length <= 10:
    print("Medium password")

else:
    print("Strong password")
