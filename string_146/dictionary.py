s = input("Enter a paragraph: ")

words = s.split()

d = {}

for word in words:
    if word in d:
        d[word] = d[word] + 1
    else:
        d[word] = 1

print("Word Frequency:")
for word in d:
    print(word, "=", d[word])