email = input("Enter your email address: ")

if "@" in email and "." in email.split("@")[-1]:
    print("Valid email address.")
else:
    print("Invalid email address.")