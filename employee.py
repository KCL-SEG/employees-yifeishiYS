"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name):
        self.name = name
        self.total_pay = 0

    def get_pay(self):
        return self.total_pay

    def __str__(self):
        employee_record = "{} works on a ".format(self.name)
        return employee_record

    def set_monthly_salary(self, salary):
        self.total_pay += salary

    def set_hourly_salary(self, time, salary):
        self.total_pay += time * salary

    def set_commission(self, num_contract, bonus):
        self.total_pay += num_contract * bonus

# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie')
billie.set_monthly_salary(4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie')
charlie.set_hourly_salary(100, 25)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee')
renee.set_monthly_salary(3000)
renee.set_commission(4, 200)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan')

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie')

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel')
