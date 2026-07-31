s = input("Enter a sentence: ")

word = ""
longest = ""

for ch in s:
    if ch != ' ':
        word = word + ch
    else:
        if len(word) > len(longest):
            longest = word
        word = ""

if len(word) > len(longest):
    longest = word

print("Longest word =", longest)