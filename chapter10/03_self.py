class Employee:
    language = "Py" #this is class attribute
    salary = 120000

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod #Sometimes we need a function that does not use the self-parameter so we write @static method
    def greet():
        print("Good morning")    

prashant = Employee()
prashant.language = "Java" # This is an instance attribute
prashant.getInfo()
prashant.greet()