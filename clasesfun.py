class Employee:
    num_of_emps = 0
    raise_amount = 1.04

    # below is constructor
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        self.dates = []
        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount)  # could also do self.raise_amount


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)
emp_1.dates.append('test');

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)
print(emp_1.dates)
