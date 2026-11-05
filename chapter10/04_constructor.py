class Employee:
    language = "Py" #this is class attribute
    salary = 120000

    def __init__(self, name, salary, language): #dunder method with is automatically called
        self.name = name
        self.salary = salary
        self.language = language

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod 
    def greet():
        print("Good morning")    

prashant = Employee("Prashant",1300000,"Javascript")
print(prashant.name, prashant.salary , prashant.language)