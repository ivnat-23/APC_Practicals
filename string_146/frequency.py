s = input("Enter a string: ")
ch = input("Enter character to find: ")

count = 0

for i in s:
    if i == ch:
        count = count + 1

print("Frequency =", count)