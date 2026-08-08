numbers = [10, 45, 23, 78, 56, 90, 34]

unique = []

for num in numbers:
    if num not in unique:
        unique.append(num)

unique.sort()

print("Second largest:", unique[-2])