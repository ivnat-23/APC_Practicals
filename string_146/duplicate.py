s = input("Enter a string: ")

for i in range(len(s)):
    count = 0
    for j in range(len(s)):
        if s[i] == s[j]:
            count = count + 1
    if count > 1:
        found = False
        for k in range(i):
            if s[i] == s[k]:
                found = True
        if found == False:
            print(s[i])