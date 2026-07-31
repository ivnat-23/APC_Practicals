s = input("Enter a string: ")

first = 0
second = 0
firstchar = ""
secondchar = ""

for i in range(len(s)):
    count = 0

    for j in range(len(s)):
        if s[i] == s[j]:
            count = count + 1

    found = False
    for k in range(i):
        if s[i] == s[k]:
            found = True

    if found == False:
        if count > first:
            second = first
            secondchar = firstchar
            first = count
            firstchar = s[i]
        elif count > second:
            second = count
            secondchar = s[i]

print("Second most frequent character =", secondchar)
print("Frequency =", second)