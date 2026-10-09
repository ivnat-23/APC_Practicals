lst = [10, 5, 20, 8, 15]

largest = second_largest = float('-inf')

for num in lst:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num

if second_largest == float('-inf'):
    print("Second largest element does not exist")
else:
    print("Second largest element:", second_largest)
