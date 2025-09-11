class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def display(self):
        print(f"Name: {self.name}, Salary: {self.salary}")
class Manager(Employee):
    def __init__(self, name, salary,department):
        super().__init__(name, salary)
        self.department=department
    def display(self):
        super().display()
        print(f"Department: {self.department}")
emp1=Employee("john",100000)
manager1=Manager("Khushi",150000,"IT")
emp1.display()
manager1.display()