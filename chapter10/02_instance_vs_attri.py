class Employee:
    language = "Py" #this is class attribute
    salary = 120000

prashant = Employee()
prashant.language = "Java" # This is an instance attribute
print( prashant.language, prashant.salary)
#  Note: Instance attributes take preference over class attributes during assignment & retrieval.     