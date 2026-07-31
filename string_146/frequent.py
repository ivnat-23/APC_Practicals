s = input("Enter a string: ")

maxcount = 0
maxchar = ""

for i in range(len(s)):
    count = 0
    for j in range(len(s)):
        if s[i] == s[j]:
            count = count + 1

    if count > maxcount:
        maxcount = count
        maxchar = s[i]

print("Most frequent character =", maxchar)
print("Frequency =", maxcount)