s = input("Enter a string: ")

result = ""
count = 1

for i in range(len(s)):
    if i == len(s) - 1:
        result = result + s[i] + str(count)
    elif s[i] == s[i + 1]:
        count = count + 1
    else:
        result = result + s[i] + str(count)
        count = 1

if len(result) < len(s):
    print(result)
else:
    print(s)