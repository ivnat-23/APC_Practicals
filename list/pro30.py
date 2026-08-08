names = ["Amit", "Rahul", "Sneha"]
ages = [25, 30, 22]
name = input("Enter patient name: ")
age = int(input("Enter patient age: "))

names.append(name)
ages.append(age)

search = input("Enter patient name to search: ")

if search in names:
    index = names.index(search)
    print("Patient found.")
    print("Name:", names[index])
    print("Age:", ages[index])
else:
    print("Patient not found.")


delete = input("Enter patient name to delete: ")

if delete in names:
    index = names.index(delete)
    names.pop(index)
    ages.pop(index)
    print("Patient deleted.")
else:
    print("Patient not found.")

print("\nAll Patients:")

for i in range(len(names)):
    print("Name:", names[i], "Age:", ages[i])
print("Total patients:", len(names))