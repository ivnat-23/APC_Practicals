marks = [
    75, 82, 65, 90, 55,
    88, 72, 95, 60, 78,
    84, 69, 91, 73, 58,
    80, 67, 89, 76, 92
]

highest = marks[0]
lowest = marks[0]
total = 0

for mark in marks:
    if mark > highest:
        highest = mark

    if mark < lowest:
        lowest = mark

    total += mark

average = total / len(marks)

above = 0
below = 0

for mark in marks:
    if mark > average:
        above += 1
    elif mark < average:
        below += 1

print("Highest marks:", highest)
print("Lowest marks:", lowest)
print("Average marks:", average)
print("Students above average:", above)
print("Students below average:", below)