class Employee:
    # skipp this class for now pass
    # below is constructor
    def __int__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'



emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee()

# we can create this even before they are created.
emp_1.first = 'Corey'
emp_1.last = 'Schafer'
emp_1.email = 'Corey.Schafer@company.com'
emp_1.pay = 50000

emp_2.first = 'Test'
emp_2.last = 'Sesr'
emp_2.email = 'Test.Sesr@company.com'
emp_2.pay = 60000

