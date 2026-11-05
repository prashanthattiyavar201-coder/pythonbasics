class Employee:
    language = "Py" #this is class attribute
    salary = 120000

prashant = Employee()
prashant.name = "prashant" # This is an instance attribute
print(prashant.name, prashant.language, prashant.salary)
      
rohan = Employee()
rohan.name = "Rohan Roho Robinson" 
print(rohan.name, rohan.language, rohan.salary)

#Here name is instance attribute and salary and language 
#attributes as they directly belong to the class

