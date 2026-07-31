password = input("Enter password: ")

upper = 0
lower = 0
digit = 0
special = 0

for ch in password:
    if ch >= 'A' and ch <= 'Z':
        upper = upper + 1
    elif ch >= 'a' and ch <= 'z':
        lower = lower + 1
    elif ch >= '0' and ch <= '9':
        digit = digit + 1
    else:
        special = special + 1

if len(password) >= 8 and upper >= 1 and lower >= 1 and digit >= 1 and special >= 1:
    print("Valid Password")
else:
    print("Invalid Password")