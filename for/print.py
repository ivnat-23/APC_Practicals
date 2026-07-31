n = int(input("Enter the value of n: "))

num = 1
limit = n ** 2

print("Series:")
while num <= limit:
    print(num, end=" ")
    num = num * 2