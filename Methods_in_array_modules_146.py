from array import array
a = array('i', [10, 20, 30, 40, 50])
print("Original Array:", a)
# 1. append()
a.append(60)
print("After append():", a)

# 2. buffer_info()
print("buffer_info():", a.buffer_info())

# 3. byteswap()
a.byteswap()
print("After byteswap():", a)

# Change it back
a.byteswap()

# 4. count()
print("count(20):", a.count(20))

# 5. extend()
a.extend([70, 80])
print("After extend():", a)

# 6. frombytes()
b = array('i')
b.frombytes(a.tobytes())
print("After frombytes():", b)

# 7. fromfile()
# First write data into a file
with open("arraydata.bin", "wb") as f:
    a.tofile(f)

c = array('i')
with open("arraydata.bin", "rb") as f:
    c.fromfile(f, len(a))

print("After fromfile():", c)

# 8. fromlist()
d = array('i')
d.fromlist([100, 200, 300])
print("After fromlist():", d)

# 9. fromunicode()
u = array('u')
u.fromunicode("Python")
print("After fromunicode():", u)

# 10. index()
print("index(30):", a.index(30))

# 11. insert()
a.insert(1, 15)
print("After insert():", a)

# 12. pop()
value = a.pop()
print("Popped value:", value)
print("After pop():", a)

# 13. remove()
a.remove(15)
print("After remove():", a)

# 14. reverse()
a.reverse()
print("After reverse():", a)

# 15. tobytes()
byte_data = a.tobytes()
print("tobytes():", byte_data)

# 16. tofile()
with open("output.bin", "wb") as f:
    a.tofile(f)
print("tofile(): Data written to output.bin")

# 17. tolist()
list_data = a.tolist()
print("tolist():", list_data)

# 18. tounicode()
u = array('u', 'Python')
print("tounicode():", u.tounicode())
