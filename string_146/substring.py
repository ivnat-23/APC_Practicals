s = input("Enter main string: ")
sub = input("Enter substring: ")

if s.find(sub) != -1:
    print("Substring found")
else:
    print("Substring not found")