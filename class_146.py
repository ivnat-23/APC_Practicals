#1.Create a class Student with attributes such as roll_no, name, and marks. Create objects for multiple students and display their details and percentage.

class Student:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks

    def display(self):
        total = sum(self.marks)
        percentage = total / len(self.marks)

        print("Roll No:", self.roll_no)
        print("Name:", self.name)
        print("Marks:", self.marks)
        print("Percentage:", percentage)
        print("----------------------")
s1 = Student(1, "Tanvi", [80, 85, 90, 75, 88])
s2 = Student(2, "Aditi", [78, 82, 85, 80, 90])
s3 = Student(3, "Rahul", [70, 75, 80, 72, 78])
s1.display()
s2.display()
s3.display()



#2.Create a class Employee with attributes emp_id, name, and basic_salary. Define methods to calculate HRA, DA, and gross salary.

class Employee:
    def __init__(self, emp_id, name, basic_salary):
        self.emp_id = emp_id
        self.name = name
        self.basic_salary = basic_salary

    def calculate(self):
        hra = 0.20 * self.basic_salary
        da = 0.10 * self.basic_salary
        gross = self.basic_salary + hra + da

        print("Employee ID:", self.emp_id)
        print("Name:", self.name)
        print("Basic Salary:", self.basic_salary)
        print("HRA:", hra)
        print("DA:", da)
        print("Gross Salary:", gross)
e = Employee(101, "Tanvi", 30000)
e.calculate()



#3.Create a class Rectangle with attributes length and breadth. Define methods to calculate area and perimeter.

class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)
r = Rectangle(10, 5)
print("Area:", r.area())
print("Perimeter:", r.perimeter())



#4.Create a class Circle with an attribute radius. Define methods to calculate the area and circumference of the circle.

class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius * self.radius

    def circumference(self):
        return 2 * 3.14 * self.radius
c = Circle(7)
print("Area of Circle:", c.area())
print("Circumference:", c.circumference()

#5.Create a class Book containing book_id, title, author, and price. Create objects for three books and display their information.

class Book:
    def __init__(self, book_id, title, author, price):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.price = price

    def display(self):
        print("Book ID:", self.book_id)
        print("Title:", self.title)
        print("Author:", self.author)
        print("Price:", self.price)
        print("----------------------")
b1 = Book(101, "Python Programming", "John", 450)
b2 = Book(102, "Java Programming", "James", 550)
b3 = Book(103, "Data Structures", "Mark", 600)
b1.display()
b2.display()
b3.display()

#6.Create a class ElectricityBill containing consumer number, consumer name, and units consumed. Define a method to calculate the electricity bill according to different unit slabs.

class ElectricityBill:
    def __init__(self, consumer_no, consumer_name, units):
        self.consumer_no = consumer_no
        self.consumer_name = consumer_name
        self.units = units

    def calculate_bill(self):
        if self.units <= 100:
            bill = self.units * 5
        elif self.units <= 200:
            bill = (100 * 5) + ((self.units - 100) * 7)
        else:
            bill = (100 * 5) + (100 * 7) + ((self.units - 200) * 10)

        print("Consumer No:", self.consumer_no)
        print("Consumer Name:", self.consumer_name)
        print("Units Consumed:", self.units)
        print("Electricity Bill: Rs.", bill)
e = ElectricityBill(1001, "Tanvi", 250)
e.calculate_bill()



#7.Create a class MobilePhone with attributes brand, model, storage, and price. Define methods to display specifications and calculate the price after discount.

class MobilePhone:
    def __init__(self, brand, model, storage, price):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.price = price

    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Storage:", self.storage)
        print("Price:", self.price)

    def discount_price(self, discount):
        final_price = self.price - (self.price * discount / 100)
        print("Price after discount:", final_price)
m = MobilePhone("Samsung", "S24", "256 GB", 70000)
m.display()
m.discount_price(10)



#8.Create a class Patient containing patient ID, name, age, disease, and consultation fee. Define methods to display patient information and calculate the total bill.

class Patient:
    def __init__(self, patient_id, name, age, disease, consultation_fee):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.disease = disease
        self.consultation_fee = consultation_fee

    def display(self):
        print("Patient ID:", self.patient_id)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Disease:", self.disease)
        print("Consultation Fee:", self.consultation_fee)

    def total_bill(self, medicine_fee):
        total = self.consultation_fee + medicine_fee
        print("Total Bill:", total)
p = Patient(101, "Rahul", 25, "Fever", 500)
p.display()
p.total_bill(1000)


#9.Design an ATM class that allows a user to check balance, deposit money, withdraw money, and display account details. Create an object and implement the operations through a menu-driven program.

class ATM:
    def __init__(self, name, account_no, balance):
        self.name = name
        self.account_no = account_no
        self.balance = balance

    def check_balance(self):
        print("Balance:", self.balance)

    def deposit(self, amount):
        self.balance += amount
        print("Amount Deposited:", amount)
        print("New Balance:", self.balance)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Amount Withdrawn:", amount)
            print("Remaining Balance:", self.balance)
        else:
            print("Insufficient Balance")

    def account_details(self):
        print("Account Holder:", self.name)
        print("Account Number:", self.account_no)
        print("Balance:", self.balance)

a = ATM("Tanvi", "123456789", 10000)

while True:
    print("\n--- ATM MENU ---")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Account Details")
    print("5. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        a.check_balance()
    elif choice == 2:
        amount = float(input("Enter amount to deposit: "))
        a.deposit(amount)
    elif choice == 3:
        amount = float(input("Enter amount to withdraw: "))
        a.withdraw(amount)
    elif choice == 4:
        a.account_details()
    elif choice == 5:
        print("Thank you!")
        break
    else:
        print("Invalid Choice")

#10.Create a class Vehicle containing vehicle number, model, rental rate, and availability. Implement methods to rent and return a vehicle and calculate rental charges based on the number of days.

class Vehicle:
    def __init__(self, vehicle_no, model, rental_rate):
        self.vehicle_no = vehicle_no
        self.model = model
        self.rental_rate = rental_rate
        self.available = True

    def rent(self):
        if self.available:
            self.available = False
            print("Vehicle rented successfully.")
        else:
            print("Vehicle is not available.")

    def return_vehicle(self):
        self.available = True
        print("Vehicle returned successfully.")

    def rental_charges(self, days):
        return self.rental_rate * days
v = Vehicle("MH10AB1234", "Swift", 1500)
v.rent()
days = int(input("Enter number of days: "))
print("Rental Charges:", v.rental_charges(days))
v.return_vehicle()

#11.Create a class ShoppingCart with customer name and cart ID. Initialize these values using a constructor. Implement methods to add products, remove products, and calculate the total bill. Use a destructor to display a message when the shopping cart object is destroyed.

class ShoppingCart:
    def __init__(self, customer_name, cart_id):
        self.customer_name = customer_name
        self.cart_id = cart_id
        self.products = []

    def add_product(self, name, price):
        self.products.append([name, price])
        print(name, "added to cart.")

    def remove_product(self, name):
        for product in self.products:
            if product[0] == name:
                self.products.remove(product)
                print(name, "removed from cart.")
                return
        print("Product not found.")

    def total_bill(self):
        total = 0
        for product in self.products:
            total += product[1]
        print("Total Bill:", total)

    def __del__(self):
        print("Shopping cart object destroyed.")


cart = ShoppingCart("Tanvi", "C101")
cart.add_product("Laptop", 50000)
cart.add_product("Mouse", 1000)
cart.add_product("Keyboard", 2000)
cart.remove_product("Mouse")
cart.total_bill()
del cart


#12.Create a class FoodOrder with order ID, customer name, food item, quantity, and price. Use a constructor to initialize the order. Define a method to calculate the total bill including tax. Implement a destructor to display an order completion message.

class FoodOrder:
    def __init__(self, order_id, customer_name, food_item, quantity, price):
        self.order_id = order_id
        self.customer_name = customer_name
        self.food_item = food_item
        self.quantity = quantity
        self.price = price

    def total_bill(self):
        amount = self.quantity * self.price
        tax = amount * 0.05
        total = amount + tax

        print("Order ID:", self.order_id)
        print("Customer Name:", self.customer_name)
        print("Food Item:", self.food_item)
        print("Quantity:", self.quantity)
        print("Price:", self.price)
        print("Tax:", tax)
        print("Total Bill:", total)

    def __del__(self):
        print("Order completed successfully.")
order = FoodOrder(101, "Tanvi", "Pizza", 2, 300)
order.total_bill()
del order



"""13. Create a class StudentResult with student name and marks in five subjects. Use a constructor to initialize the details.
Define methods to calculate total, percentage, and grade. Implement a destructor to display a suitable message."""

class StudentResult:
    def __init__(self, name, m1, m2, m3, m4, m5):
        self.name = name
        self.marks = [m1, m2, m3, m4, m5]

    def total(self):
        return sum(self.marks)

    def percentage(self):
        return self.total() / 5

    def grade(self):
        percentage = self.percentage()

        if percentage >= 90:
            return "A+"
        elif percentage >= 80:
            return "A"
        elif percentage >= 70:
            return "B"
        elif percentage >= 60:
            return "C"
        elif percentage >= 50:
            return "D"
        else:
            return "F"

    def display(self):
        print("Student Name:", self.name)
        print("Marks:", self.marks)
        print("Total:", self.total())
        print("Percentage:", self.percentage())
        print("Grade:", self.grade())

    def __del__(self):
        print("Student result object destroyed.")


s = StudentResult("Tanvi", 85, 90, 78, 88, 92)
s.display()
del s

