class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

class Employee(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id

    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Employee ID: {self.employee_id}")

class PartTime(Person):
    def __init__(self, name, age, working_hours):
        super().__init__(name, age)
        self.working_hours = working_hours

    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Working Hours: {self.working_hours} hrs/week")

class Consultant(Employee, PartTime):
    def __init__(self, name, age, employee_id, working_hours, project_name):
        Employee.__init__(self, name, age, employee_id)
        PartTime.__init__(self, name, age, working_hours)
        self.project_name = project_name

    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Employee ID: {self.employee_id}")
        print(f"Working Hours: {self.working_hours} hrs/week")
        print(f"Project Name: {self.project_name}")

person1 = Person("Amit", 30)
employee1 = Employee("Ravi", 28, "E102")
parttime1 = PartTime("Sneha", 22, 20)
consultant1 = Consultant("Anjali", 35, "C203", 25, "AI Development")

print("---- Person ----")
person1.show_details()
print("\n---- Employee ----")
employee1.show_details()
print("\n---- Part-Time Worker ----")
parttime1.show_details()
print("\n---- Consultant ----")
consultant1.show_details()
