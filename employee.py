"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""


class Employee:
    def __init__(self, name, monthly_salary=0, hourly_salary=0, hours=0, num_contracts=0, commission=0, bonus=0):
        self.name = name
        self.total_pay = 0
        self.monthly_salary = monthly_salary
        self.hourly_salary = hourly_salary
        self.hours = hours
        self.num_contracts = num_contracts
        self.commission = commission
        self.bonus = bonus

        self.is_monthly = False if monthly_salary == 0 else True
        self.is_commission = False if num_contracts == 0 else True
        self.is_bonus = False if bonus == 0 else True

        self.cal_total_pay()

    def get_pay(self):
        return self.total_pay

    def cal_total_pay(self):
        self.total_pay += self.monthly_salary + self.hourly_salary * self.hours + \
                          self.bonus + self.commission * self.num_contracts

    def __str__(self):
        work_type = "monthly salary of {}".format(self.monthly_salary) if self.is_monthly else \
            "contract of {} hours at {}/hour".format(self.hours, self.hourly_salary)
        commission = " and receives a commission for {} contract(s) at {}/contract".format(self.num_contracts, self.commission) if self.is_commission else ""
        bonus = " and receives a bonus commission of {}".format(self.bonus) if self.is_bonus else ""
        total = ".  Their total pay is {}.".format(self.total_pay)
        employee_record = "{} works on a ".format(self.name) + work_type + commission + bonus + total
        return employee_record


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', 4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', 0, 25, 100)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', 3000, 0, 0, 4, 200, 0)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', 0, 25, 150, 3, 220, 0)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', 2000, 0, 0, 0, 0, 1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', 0, 30, 120, 0, 0, 600)