marital = input("Enter marital status (married/unmarried): ").lower()

if marital == "married":
    print("The driver is insured")
else:
    gender = input("Enter gender (male/female): ").lower()
    age = int(input("Enter age: "))

    if (gender == "male" and age > 30) or (gender == "female" and age > 25):
        print("The driver is insured")
    else:
        print("The driver is not insured")