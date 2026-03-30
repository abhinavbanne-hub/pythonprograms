# Base class 1
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


# Base class 2
class Employee:
    def __init__(self, employee_id, salary):
        self.employee_id = employee_id
        self.salary = salary

    def display_employee_info(self):
        print(f"Employee ID: {self.employee_id}")
        print(f"Salary: {self.salary}")


# Derived class (inherits from both Person and Employee)
class Manager(Person, Employee):
    def __init__(self, name, age, employee_id, salary, department):
        # Initialize both parent classes
        Person.__init__(self, name, age)
        Employee.__init__(self, employee_id, salary)

        # Manager-specific attribute
        self.department = department

    # Additional method specific to Manager
    def display_manager_info(self):
        print(f"Department: {self.department}")

    def give_bonus(self, amount):
        self.salary += amount
        print(f"Bonus added! New salary: {self.salary}")


# Creating an object of Manager
mgr = Manager("Abhinav", 30, "M101", 75000, "IT")

# Accessing methods from Person
mgr.display_person_info()

# Accessing methods from Employee
mgr.display_employee_info()

# Accessing Manager-specific methods
mgr.display_manager_info()
mgr.give_bonus(5000)
