#1.Write a Python program to create a set containing five integers and display all its elements.
s=(12,13,14,15,16)
print("set",s)

#2.Create a list containing duplicate values. Convert the list into a set and display the resulting set.
L = [10, 20, 30, 20, 40, 10, 50]
S = set(L)
print("List:", L)
print("Set:", S)

#3.Create a set of five fruits. Add two new fruits using appropriate set methods and display the updated set.
s = {"apple", "banana", "pear", "grapes", "mango"}
s.add("orange")
s.add("watermelon")
print(s)

#4.Create a set of numbers and remove a specified number from the set.
s = {10, 20, 30, 40, 50}
s.remove(30)
print(s)

#5.Create a set of student names. Ask the user to enter a name and check whether the student exists in the set.
students = {"Tanvi", "Rahul", "Priya", "Amit", "Sneha"}
name = input("Enter student name: ")
if name in students:
    print("Student exists in the set")
else:
    print("Student does not exist in the set")

#6.Create a set of cities and determine the total number of cities using an appropriate function.
cities = {"Pune", "Mumbai", "Delhi", "Kolkata", "Chennai"}
print("Total number of cities:", len(cities))

#7.Create a set of programming languages and display each language using a for loop.
languages = {"Python", "Java", "C", "C++", "JavaScript"}
for language in languages:
    print(language)

#8.Create a list containing duplicate numbers, use a set to remove the duplicates.
numbers = [10, 20, 30, 20, 40, 10, 50, 30]
unique_numbers = set(numbers)
print("Original List:", numbers)
print("After Removing Duplicates:", unique_numbers)

#9.Create two sets of integers and find their union.
A = {10, 20, 30, 40}
B = {30, 40, 50, 60}
result = A.union(B)
print("Union:", result)

#10.Create two sets and find the elements common to both sets.
A = {10, 20, 30, 40}
B = {30, 40, 50, 60}
result = A.intersection(B)
print("Common elements:", result)

"""11.Create two sets and find:
	Elements present in the first set but not the second 
	Elements present in the second set but not the first"""
A = {10, 20, 30, 40}
B = {30, 40, 50, 60}
print("First set but not second:", A.difference(B))
print("Second set but not first:", B.difference(A))

#12. Create two sets of numbers and find the elements that are present in either set but not in both.
A = {10, 20, 30, 40}
B = {30, 40, 50, 60}
result = A.symmetric_difference(B)
print("Elements present in either set but not both:", result)

#13.Create two sets and determine whether the first set is a subset of the second set.
A = {10, 20}
B = {10, 20, 30, 40}
if A.issubset(B):
    print("First set is a subset of the second set")
else:
    print("First set is not a subset of the second set")

#14.Create two sets and determine whether the first set is a superset of the second set.
A = {10, 20, 30, 40}
B = {10, 20}
if A.issuperset(B):
    print("First set is a superset of the second set")
else:
    print("First set is not a superset of the second set")


#15.Write a program to determine whether two sets have no elements in common.
A = {10, 20, 30}
B = {40, 50, 60}

if A.isdisjoint(B):
    print("The sets have no elements in common")
else:
    print("The sets have elements in common")

#16.Create two sets and check whether they are equal.
A = {10, 20, 30}
B = {30, 20, 10}

if A == B:
    print("Both sets are equal")
else:
    print("Both sets are not equal")

#17.Two students have selected different subjects. Store their subjects in two sets and determine the subjects studied by both students.
student1 = {"Python", "Java", "DBMS", "Maths"}
student2 = {"Java", "DBMS", "OS", "Networks"}

common = student1.intersection(student2)

print("Subjects studied by both students:", common)

#18.Accept a sentence from the user and use a set to display all unique words.
sentence = input("Enter a sentence: ")
words = set(sentence.split())
print("Unique words:", words)

"""19.Create two sets:
•Students present in the morning session 
•Students present in the afternoon session 
Find:
•Students present in both sessions 
•Students present only in the morning 
•Students present only in the afternoon 
•Students present in at least one session"""
morning = {"Tanvi", "Rahul", "Priya", "Amit", "Sneha"}
afternoon = {"Priya", "Amit", "Riya", "Karan", "Neha"}

print("Students present in both sessions:", morning.intersection(afternoon))
print("Students present only in morning:", morning.difference(afternoon))
print("Students present only in afternoon:", afternoon.difference(morning))
print("Students present in at least one session:", morning.union(afternoon))

"""20.Create sets representing students enrolled in:
•Python 
•Java """
python_students = {"Tanvi", "Rahul", "Priya", "Amit"}
java_students = {"Priya", "Amit", "Sneha", "Riya"}

print("Python Students:", python_students)
print("Java Students:", java_students)

"""21.Create two sets representing technical skills of two employees. Find:
•Common skills 
•Skills unique to Employee 1 
•Skills unique to Employee 2 
•All available skills"""
employee1 = {"Python", "Java", "SQL", "HTML", "CSS"}
employee2 = {"Python", "JavaScript", "SQL", "React", "CSS"}

print("Common skills:", employee1.intersection(employee2))
print("Skills unique to Employee 1:", employee1.difference(employee2))
print("Skills unique to Employee 2:", employee2.difference(employee1))
print("All available skills:", employee1.union(employee2))

#22.Find students enrolled in both courses and students enrolled in only one course.
python_students = {"Tanvi", "Rahul", "Priya", "Amit"}
java_students = {"Priya", "Amit", "Sneha", "Riya"}

both_courses = python_students.intersection(java_students)
only_one_course = python_students.symmetric_difference(java_students)

print("Students enrolled in both courses:", both_courses)
print("Students enrolled in only one course:", only_one_course)

"""23.Store visitor IDs from two different days in separate sets. Determine:
•Unique visitors across both days 
•Returning visitors 
•Visitors who came only on the first day 
•Visitors who came only on the second day
•Create sets representing products belonging to different categories. Find products that belong to both categories"""
day1 = {101, 102, 103, 104, 105}
day2 = {103, 104, 105, 106, 107}

unique_visitors = day1.union(day2)
returning_visitors = day1.intersection(day2)
first_day_only = day1.difference(day2)
second_day_only = day2.difference(day1)

print("Unique visitors:", unique_visitors)
print("Returning visitors:", returning_visitors)
print("First day only:", first_day_only)
print("Second day only:", second_day_only)

#24.Create a set containing available books and another set containing requested books. Determine which requested books are available.
available_books = {"Python", "Java", "DBMS", "Networking"}
requested_books = {"Python", "DBMS", "C++", "HTML"}

available_requested = available_books.intersection(requested_books)

print("Requested books that are available:", available_requested)

"""25.Store visitor IDs from two different days in separate sets. Determine:
•Unique visitors across both days 
•Returning visitors 
•Visitors who came only on the first day 
•Visitors who came only on the second day
•Create sets representing products belonging to different categories. Find products that belong to both categories."""
day1 = {101, 102, 103, 104, 105}
day2 = {103, 104, 105, 106, 107}

print("Unique visitors:", day1.union(day2))
print("Returning visitors:", day1.intersection(day2))
print("First day only:", day1.difference(day2))
print("Second day only:", day2.difference(day1))





