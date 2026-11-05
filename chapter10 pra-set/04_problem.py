class Calculator:
    def __init__(self, n):
        self.n = n

    def square(self):
        print(f"The square is {self.n*self.n}")

    def cube(self):
        print(f"The cube is {self.n*self.n*self.n}")

    def squareRoot(self):
        print(f"The squareRoot is {self.n**1/2}")

    @staticmethod
    def hello():
        print("Hey Hii")        

n = int(input("Enter a number: "))

a = Calculator(n)
a.hello()
a.square()
a.cube()
a.squareRoot()