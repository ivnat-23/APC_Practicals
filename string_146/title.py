s = input("Enter a sentence: ")

result = ""
newword = True

for ch in s:
    if newword and ch >= 'a' and ch <= 'z':
        result = result + chr(ord(ch) - 32)
        newword = False
    else:
        result = result + ch
        if ch == ' ':
            newword = True
        else:
            newword = False

print("Title Case =", result)