#1.Write a Python program to create a file named student.txt and write the student's name, roll number, branch, and semester into the file.  

name = input("Enter student name: ")
roll_no = input("Enter roll number: ")
branch = input("Enter branch: ")
semester = input("Enter semester: ")

file = open("student.txt", "w")

file.write("Student Name: " + name + "\n")
file.write("Roll Number: " + roll_no + "\n")
file.write("Branch: " + branch + "\n")
file.write("Semester: " + semester + "\n")

file.close()

print("Student details written successfully to student.txt")

#2. Write a program to open a text file and display its complete contents.
file = open("student.txt", "r")
content = file.read()
print("File Contents:")
print(content)
file.close()

#3.Write a program to append additional student information to an existing file without deleting its previous contents.  

name = input("Enter student name: ")
roll_no = input("Enter roll number: ")
branch = input("Enter branch: ")
semester = input("Enter semester: ")

file = open("student.txt", "a")

file.write("\nStudent Name: " + name + "\n")
file.write("Roll Number: " + roll_no + "\n")
file.write("Branch: " + branch + "\n")
file.write("Semester: " + semester + "\n")

file.close()

print("Student information appended successfully.")

#4. Read a text file line by line and display each line separately
file = open("student.txt", "r")
for line in file:
    print(line.strip())
file.close()

#5.Count and display the total number of lines in a text file.
file = open("student.txt", "r")
count = 0
for line in file:
    count += 1
print("Total number of lines:", count)
file.close()

#6. Count the total number of words present in a text file
file = open("student.txt", "r")
count = 0
for line in file:
    words = line.split()
    count += len(words)
print("Total number of words:", count)
file.close()

#7.Count total number of characters in a text file, including spaces.
file = open("student.txt", "r")
content = file.read()
count = len(content)
print("Total number of characters:", count)
file.close()

#8.Read a text file and display its lines in reverse order.
file = open("student.txt", "r")
lines = file.readlines()
for line in reversed(lines):
    print(line.strip())
file.close()

#9.Count the number of vowels and consonants in a text file
file = open("student.txt", "r")
content = file.read()
vowels = 0
consonants = 0
for ch in content:
    if ch.isalpha():
        if ch.lower() in "aeiou":
            vowels += 1
        else:
            consonants += 1
print("Total vowels:", vowels)
print("Total consonants:", consonants)
file.close()

#10. Count alphabets, digits, spaces and special characters
file = open("student.txt", "r")
content = file.read()
alphabets = 0
digits = 0
spaces = 0
special = 0
for ch in content:
    if ch.isalpha():
        alphabets += 1
    elif ch.isdigit():
        digits += 1
    elif ch == " ":
        spaces += 1
    else:
        special += 1
print("Total alphabets:", alphabets)
print("Total digits:", digits)
print("Total spaces:", spaces)
print("Total special characters:", special)
file.close()

#11.Find the longest word in a text file
file = open("student.txt", "r")
words = file.read().split()
longest = max(words, key=len)
print("Longest word:", longest)
file.close()

#12.Count how many times each word occurs using a dictionary
file = open("student.txt", "r")
words = file.read().split()
count = {}
for word in words:
    count[word] = count.get(word, 0) + 1
print(count)
file.close()

#13.Search for a word and display occurrences and line numbers
word = input("Enter word to search: ")
file = open("student.txt", "r")
count = 0
lines = []
for number, line in enumerate(file, 1):
    words = line.split()
    if word in words:
        count += words.count(word)
        lines.append(number)
print("Occurrences:", count)
print("Line numbers:", lines)
file.close()

#14.Replace a word with another word and save in a new file
old = input("Enter word to replace: ")
new = input("Enter new word: ")
file = open("student.txt", "r")
content = file.read()
file.close()
content = content.replace(old, new)
file = open("newstudent.txt", "w")
file.write(content)
file.close()
print("File modified successfully.")

#15. Remove single-line comments from a Python file
file = open("program.py", "r")
output = open("without_comments.py", "w")
for line in file:
    if not line.strip().startswith("#"):
        output.write(line)
file.close()
output.close()
print("Comments removed successfully.")

#16. Create another file containing the text in uppercase
file = open("student.txt", "r")
content = file.read()
file.close()
output = open("uppercase.txt", "w")
output.write(content.upper())
output.close()
print("Uppercase file created successfully.")

"""17.Create a file containing student records in the format:
RollNo,Name,Marks
101,Amit,85
102,Priya,92
103,Rahul,78
Write a program to:
• Display all records.
• Find the student with the highest marks.
• Calculate average marks.
• Display students who scored more than 80."""
file = open("students.txt", "w")
file.write("RollNo,Name,Marks\n")
file.write("101,Amit,85\n")
file.write("102,Priya,92\n")
file.write("103,Rahul,78\n")
file.close()

file = open("students.txt", "r")
records = file.readlines()
file.close()

print("All Records:")
for record in records:
    print(record.strip())

students = []

for record in records[1:]:
    roll, name, marks = record.strip().split(",")
    students.append((roll, name, int(marks)))

highest = max(students, key=lambda x: x[2])
print("\nStudent with highest marks:")
print(highest[0], highest[1], highest[2])

total = sum(student[2] for student in students)
average = total / len(students)
print("\nAverage marks:", average)

print("\nStudents who scored more than 80:")
for student in students:
    if student[2] > 80:
        print(student[0], student[1], student[2])

"""18. Store employee ID, name, department, and salary in a file. Write functions to:
• Display all employees.
• Find the highest-paid employee.
Calculate average salary.
• Display employees earning above a given salary."""
def display_employees():
    file = open("employee.txt", "r")
    print("Employee Records:")
    for line in file:
        print(line.strip())
    file.close()

def highest_salary():
    file = open("employee.txt", "r")
    employees = []
    for line in file:
        emp_id, name, department, salary = line.strip().split(",")
        employees.append((emp_id, name, department, float(salary)))
    file.close()
    employee = max(employees, key=lambda x: x[3])
    print("Highest Paid Employee:", employee)

def average_salary():
    file = open("employee.txt", "r")
    total = 0
    count = 0
    for line in file:
        data = line.strip().split(",")
        total += float(data[3])
        count += 1
    file.close()
    print("Average Salary:", total / count)

def above_salary(amount):
    file = open("employee.txt", "r")
    print("Employees earning above", amount)
    for line in file:
        data = line.strip().split(",")
        if float(data[3]) > amount:
            print(line.strip())
    file.close()

file = open("employee.txt", "w")
file.write("101,Amit,IT,50000\n")
file.write("102,Priya,HR,60000\n")
file.write("103,Rahul,Finance,45000\n")
file.write("104,Neha,IT,75000\n")
file.close()

display_employees()
highest_salary()
average_salary()

salary = float(input("Enter salary: "))
above_salary(salary)

#19. Store student attendance records in a file. Calculate the attendance percentage and display students having attendance below 75%.
def attendance_percentage(attended, total):
    return (attended / total) * 100

def display_low_attendance():
    file = open("attendance.txt", "r")
    print("Students having attendance below 75%:")
    for line in file:
        roll, name, attended, total = line.strip().split(",")
        percentage = attendance_percentage(int(attended), int(total))
        if percentage < 75:
            print(roll, name, round(percentage, 2), "%")
    file.close()

file = open("attendance.txt", "w")
file.write("101,Amit,35,50\n")
file.write("102,Priya,45,50\n")
file.write("103,Rahul,30,50\n")
file.write("104,Neha,40,50\n")
file.close()

display_low_attendance()



"""20. Store deposits and withdrawals in a file. Read the file and calculate:
• Total deposits
• Total withdrawals
• Final balance
• Largest transaction"""
file = open("bank.txt", "w")
file.write("D,5000\n")
file.write("W,2000\n")
file.write("D,3000\n")
file.write("W,1000\n")
file.close()

file = open("bank.txt", "r")
total_deposits = 0
total_withdrawals = 0
largest_transaction = 0

for line in file:
    type, amount = line.strip().split(",")
    amount = float(amount)

    if type == "D":
        total_deposits += amount
    elif type == "W":
        total_withdrawals += amount

    if amount > largest_transaction:
        largest_transaction = amount

file.close()

final_balance = total_deposits - total_withdrawals

print("Total deposits:", total_deposits)
print("Total withdrawals:", total_withdrawals)
print("Final balance:", final_balance)
print("Largest transaction:", largest_transaction)

"""21. Maintain book records containing book ID, title, author, and availability status.
Implement operations to:
• Add a book.
• Search for a book.
• Issue a book.
• Return a book.
• Display available books."""
def add_book():
    file = open("books.txt", "a")
    book_id = input("Enter book ID: ")
    title = input("Enter title: ")
    author = input("Enter author: ")
    file.write(book_id + "," + title + "," + author + ",Available\n")
    file.close()
    print("Book added successfully.")

def search_book():
    book_id = input("Enter book ID to search: ")
    file = open("books.txt", "r")
    found = False
    for line in file:
        data = line.strip().split(",")
        if data[0] == book_id:
            print("Book found:", line.strip())
            found = True
    if not found:
        print("Book not found.")
    file.close()

def issue_book():
    book_id = input("Enter book ID to issue: ")
    file = open("books.txt", "r")
    books = file.readlines()
    file.close()
    file = open("books.txt", "w")
    for line in books:
        data = line.strip().split(",")
        if data[0] == book_id and data[3] == "Available":
            data[3] = "Issued"
        file.write(",".join(data) + "\n")
    file.close()
    print("Book issued successfully.")

def return_book():
    book_id = input("Enter book ID to return: ")
    file = open("books.txt", "r")
    books = file.readlines()
    file.close()
    file = open("books.txt", "w")
    for line in books:
        data = line.strip().split(",")
        if data[0] == book_id:
            data[3] = "Available"
        file.write(",".join(data) + "\n")
    file.close()
    print("Book returned successfully.")

def display_available():
    file = open("books.txt", "r")
    print("Available Books:")
    for line in file:
        data = line.strip().split(",")
        if data[3] == "Available":
            print(line.strip())
    file.close()

file = open("books.txt", "w")
file.write("101,Python Basics,John,Available\n")
file.write("102,Data Structures,James,Available\n")
file.write("103,Computer Networks,David,Issued\n")
file.close()

while True:
    print("\n1. Add Book")
    print("2. Search Book")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Display Available Books")
    print("6. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        add_book()
    elif choice == 2:
        search_book()
    elif choice == 3:
        issue_book()
    elif choice == 4:
        return_book()
    elif choice == 5:
        display_available()
    elif choice == 6:
        break
    else:
        print("Invalid choice")


#22. Read the contents of two text files and create a third file containing the contents of both files.
file1 = open("file1.txt", "r")
content1 = file1.read()
file1.close()

file2 = open("file2.txt", "r")
content2 = file2.read()
file2.close()

file3 = open("file3.txt", "w")
file3.write(content1)
file3.write("\n")
file3.write(content2)
file3.close()

print("Contents combined successfully.")        
        

#23. Write a program to compare two text files and display whether their contents are identical. If different, identify the first line where they differ.
file1 = open("file1.txt", "r")
file2 = open("file2.txt", "r")

lines1 = file1.readlines()
lines2 = file2.readlines()

file1.close()
file2.close()

if lines1 == lines2:
    print("Both files are identical.")
else:
    print("Files are different.")
    length = min(len(lines1), len(lines2))
    found = False

    for i in range(length):
        if lines1[i] != lines2[i]:
            print("First difference is at line:", i + 1)
            print("File 1:", lines1[i].strip())
            print("File 2:", lines2[i].strip())
            found = True
            break

    if not found:
        print("One file has additional lines.")
