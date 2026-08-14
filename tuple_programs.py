#1.Write a Python program to create a tuple of five integers and display it.
numbers=(10,20,30,40,50)
print("the tuple is:",numbers)


"""2.Create a tuple containing five city names. Display:
	First city 
	Last city 
	Third city"""

cities = ("Pune", "Mumbai", "Delhi", "Kolkata", "Chennai")
print("First city:", cities[0])
print("Last city:", cities[-1])
print("Third city:", cities[2])


#3.Create a tuple of student names and display the total number of students using the len() function.
students = ("Tanvi", "Rahul", "Sneha", "Amit", "Priya")
print("Total number of students:", len(students))


#4.Create a tuple of colors. Check whether a given color exists in the tuple
colors = ("Red", "Blue", "Green", "Yellow", "Black")
color = "Green"
if color in colors:
    print("Color exists in the tuple")
else:
    print("Color does not exist in the tuple")

    
#5.Create a tuple of fruits and display each fruit using a loop.
fruits = ("Apple", "Banana", "Mango", "Orange", "Grapes")
for fruit in fruits:
    print(fruit)

    
#6.Create a tuple with repeated numbers and count how many times a particular number appears.
numbers = (10, 20, 10, 30, 10, 40, 20)
print(numbers.count(10))


#7.Create a tuple of employee IDs and find the index of a given ID.
employee_id=(101,102,103,104,105)
print(employee_id.index(103))


#8.Create two tuples of numbers and concatenate them into a single tuple.
tuple1 = (10, 20, 30)
tuple2 = (40, 50, 60)
result = tuple1 + tuple2
print(result)


#9.Create a tuple containing three elements and repeat it four times.
tuple1 = (10, 20, 30)
result = tuple1 * 4
print(result)


"""10.Create a tuple of 10 numbers and display:
	First five elements 
	Last five elements 
	Middle four elements 
	Alternate elements 
	Reverse tuple"""
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

print("First five elements:", numbers[:5])
print("Last five elements:", numbers[5:])
print("Middle four elements:", numbers[3:7])
print("Alternate elements:", numbers[::2])
print("Reverse tuple:", numbers[::-1])


#11.Convert a tuple into a list and add a new element.
numbers = (10, 20, 30, 40)
numbers = list(numbers)
numbers.append(50)
print(numbers)


#12.Accept five numbers from the user, store them in a list, and convert the list into a tuple.
numbers = []

for i in range(5):
    num = int(input("Enter a number: "))
    numbers.append(num)

numbers = tuple(numbers)

print(numbers)


#13.Modify a tuple by converting it into a list and then back into a tuple.
numbers = (10, 20, 30, 40)

numbers = list(numbers)
numbers[1] = 50

numbers = tuple(numbers)

print(numbers)


#14.Create a tuple and delete it completely.
numbers = (10, 20, 30, 40)

del numbers

print("Tuple deleted")


#15.Create a nested tuple containing student details and display each record.
students = (("Tanvi", 20), ("Rahul", 21), ("Sneha", 20))

for student in students:
    print(student)

#16.Store ten numbers in a tuple and calculate their sum.
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(sum(numbers))

#17.Find the largest and smallest number in a tuple without using `max()` and `min()`.
numbers = (10, 25, 5, 40, 15)

largest = numbers[0]
smallest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num

print("Largest:", largest)
print("Smallest:", smallest)

#18.Calculate the average of elements stored in a tuple.
numbers = (10, 20, 30, 40, 50)
average = sum(numbers) / len(numbers)
print("Average:", average)

"""19.Store 15 integers in a tuple and count:
	Even numbers 
	Odd numbers"""
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)
even = 0
odd = 0
for num in numbers:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1
print("Even numbers:", even)
print("Odd numbers:", odd)

#20.Accept a number from the user and determine whether it exists in the tuple.
numbers = (10, 20, 30, 40, 50)
num = int(input("Enter a number: "))
if num in numbers:
    print("Number exists in the tuple")
else:
    print("Number does not exist in the tuple")

"""21.Store student details in a tuple:
	Roll Number 
	Name 
	Department 
	Marks 
Display all the details."""
student = (101, "Tanvi", "Computer Engineering", 92)
print("Roll Number:", student[0])
print("Name:", student[1])
print("Department:", student[2])
print("Marks:", student[3])


"""22.Create tuples containing:
	Employee ID 
	Name 
	Salary"""
employee = (101, "Tanvi", 50000)
print("Employee ID:", employee[0])
print("Name:", employee[1])
print("Salary:", employee[2])

"""23.	Store item prices in a tuple and calculate
        Total bill 
	Average price 
	Highest-priced item 
	Lowest-priced item"""
prices = (100, 250, 150, 300, 200)
total = sum(prices)
average = total / len(prices)
highest = max(prices)
lowest = min(prices)
print("Total bill:", total)
print("Average price:", average)
print("Highest-priced item:", highest)
print("Lowest-priced item:", lowest)


"""24.	Store temperatures of seven days in a tuple and determine:
•	Maximum temperature 
•	Minimum temperature 
•	Average temperature """
temperatures = (30, 32, 29, 31, 33, 28, 30)

maximum = max(temperatures)
minimum = min(temperatures)
average = sum(temperatures) / len(temperatures)

print("Maximum temperature:", maximum)
print("Minimum temperature:", minimum)
print("Average temperature:", average)


"""25.Store runs scored in 10 matches and calculate:
•	Total runs 
•	Highest score 
•	Lowest score 
•	Average score """
runs = (45, 78, 32, 90, 56, 67, 23, 81, 49, 70)
total = sum(runs)
highest = max(runs)
lowest = min(runs)
average = total / len(runs)
print("Total runs:", total)
print("Highest score:", highest)
print("Lowest score:", lowest)
print("Average score:", average)

#26.Merge two tuples and remove duplicate elements.
tuple1 = (10, 20, 30, 40, 50)
tuple2 = (30, 40, 50, 60, 70)
common = tuple(x for x in tuple1 if x in tuple2)
print("Common elements:", common)

#27.Merge two tuples and remove duplicate elements.
tuple1 = (10, 20, 30, 40)
tuple2 = (30, 40, 50, 60)
merged = tuple(set(tuple1 + tuple2))
print("Merged tuple:", merged)


#28.Count the frequency of each element in a tuple.
numbers = (10, 20, 10, 30, 20, 10, 40)
for num in set(numbers):
    print(num, ":", numbers.count(num))

#29.Convert a tuple into a sorted tuple in ascending and descending order.
numbers = (40, 10, 30, 20, 50)
ascending = tuple(sorted(numbers))
descending = tuple(sorted(numbers, reverse=True))
print("Ascending:", ascending)
print("Descending:", descending)

"""30.Create a tuple containing patient records:
	Patient ID 
	Name 
	Age 
	Blood Group 
Perform the following operations:
	Display all records 
	Search for a patient by ID 
	Count the total number of patients 
	Display patients with a specific blood group """
patients = (
    (101, "Tanvi", 20, "O+"),
    (102, "Rahul", 21, "A+"),
    (103, "Sneha", 22, "O+"),
    (104, "Amit", 20, "B+")
)
print("All patient records:")
for patient in patients:
    print(patient)

patient_id = 103
for patient in patients:
    if patient[0] == patient_id:
        print("Patient found:", patient)

print("Total number of patients:", len(patients))
blood_group = "O+"
print("Patients with blood group", blood_group)
for patient in patients:
    if patient[3] == blood_group:
        print(patient)








    




