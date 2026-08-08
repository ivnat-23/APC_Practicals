scores = [45, 102, 78, 56, 120, 34, 89, 150, 67, 42]

highest = scores[0]
lowest = scores[0]
total = 0
centuries = 0
half_centuries = 0

for score in scores:

    if score > highest:
        highest = score

    if score < lowest:
        lowest = score

    total += score

    if score >= 100:
        centuries += 1

    elif score >= 50:
        half_centuries += 1

average = total / len(scores)

print("Highest score:", highest)
print("Lowest score:", lowest)
print("Total runs:", total)
print("Average runs:", average)
print("Centuries:", centuries)
print("Half-centuries:", half_centuries)