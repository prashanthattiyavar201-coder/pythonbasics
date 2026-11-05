def divisible(n):
    if(n%5 == 0):
        return True
    return False

a = [1,2,34234,53,654321,7654321,65,734,45,55]

f = list(filter(divisible, a))
print(f)