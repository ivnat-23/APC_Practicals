import csv


def add_student():
    roll = input("Enter roll number: ")
    name = input("Enter student name: ")
    m1 = int(input("Enter Maths marks: "))
    m2 = int(input("Enter Science marks: "))
    m3 = int(input("Enter English marks: "))

    total = m1 + m2 + m3
    percentage = total / 3

    if percentage >= 90:
        grade = "A"
    elif percentage >= 75:
        grade = "B"
    elif percentage >= 50:
        grade = "C"
    else:
        grade = "F"

    with open("students.csv", "a", newline="") as f:
        w = csv.writer(f)
        w.writerow([roll, name, m1, m2, m3,
                    total, percentage, grade])

    print("Student record saved!")


# Display student records
def display_students():
    try:
        with open("students.csv", "r") as f:
            reader = csv.reader(f)
            for row in reader:
                print(row)
    except FileNotFoundError:
        print("No records found.")


# Find the topper
def find_topper():
    try:
        with open("students.csv", "r") as f:
            students = list(csv.reader(f))

        if not students:
            print("No student records found.")
            return

        topper = max(students, key=lambda x: float(x[5]))
        print("Class topper:", topper[1])
        print("Total marks:", topper[5])

    except FileNotFoundError:
        print("No records found.")


# Display class statistics
def statistics():
    try:
        with open("students.csv", "r") as f:
            students = list(csv.reader(f))

        if not students:
            print("No records found.")
            return

        percentages = [float(s[6]) for s in students]

        print("Number of students:", len(students))
        print("Class average:", sum(percentages) / len(percentages))
        print("Highest percentage:", max(percentages))
        print("Lowest percentage:", min(percentages))

    except FileNotFoundError:
        print("No records found.")


# Main menu
while True:
    print("\n1. Add Student")
    print("2. Display Students")
    print("3. Find Topper")
    print("4. Show Statistics")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        display_students()
    elif choice == "3":
        find_topper()
    elif choice == "4":
        statistics()
    elif choice == "5":
        break
    else:
        print("Invalid choice")
