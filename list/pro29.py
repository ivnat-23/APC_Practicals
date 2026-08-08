temperatures = [
    28, 30, 32, 29, 31,
    35, 33, 30, 27, 26,
    29, 34, 36, 31, 28,
    25, 27, 30, 32, 35,
    37, 33, 29, 28, 31,
    34, 36, 32, 30, 29
]

hottest = temperatures[0]
coldest = temperatures[0]
total = 0

for temp in temperatures:

    if temp > hottest:
        hottest = temp

    if temp < coldest:
        coldest = temp

    total += temp

average = total / len(temperatures)

above = 0
below = 0

for temp in temperatures:
    if temp > average:
        above += 1
    elif temp < average:
        below += 1

print("Hottest temperature:", hottest)
print("Coldest temperature:", coldest)
print("Average temperature:", average)
print("Days above average:", above)
print("Days below average:", below)