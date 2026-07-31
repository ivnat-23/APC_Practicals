s1 = input("Enter first string: ").lower()
s2 = input("Enter second string: ").lower()

temp = s1 + s1

if s2 in temp:
    print("Yes")
else:
    print("No")