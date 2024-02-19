class Employee:
    def __init__(self, name, age, salary):
        self.name=name
        self.age=age
        self.salary=salary

    def bonus(self, bonusv):
        return bonusv*self.salary/100
    
    def is_young(self):
        return self.age<30
    
    def sort_employees(self, )