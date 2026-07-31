email = input("Enter email: ")

if email.count("@") == 1 and "." in email and email.index("@") < email.rindex("."):
    print("Valid Email")
else:
    print("Invalid Email")