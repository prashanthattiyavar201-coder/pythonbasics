class programmer:
    company = "Microsoft"
    def __init__(self, name, salary, pincode):
        self.name = name
        self.salary = salary
        self.pincode = pincode

p = programmer("Prashant", 1200000, 591102)
print(p.name, p.salary, p.pincode)

r = programmer("rohan", 1200000, 591102)
print(r.name, r.salary, r.pincode)