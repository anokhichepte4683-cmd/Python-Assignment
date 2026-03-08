class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
class Employee(Person):
    def __init__(self,name,age,employee_id,salary):
        Person.__init__(self,name,age)
        self.employee_id = employee_id
        self.salary = salary
class Manager(Employee):
    def __init__(self,name,age,employee_id,salary,department):
        Employee.__init__(self,name,age,employee_id,salary)
        self.department = department
    def display(self):
     print("Name",self.name)
     print(" age",self.age)
     print("employee_id",self.employee_id)
     print("salary",self.salary)
     print("department",self.department)
     
     
m1 = Manager("Aila chan",18,"E123",100000,"CSE")
m1.display()