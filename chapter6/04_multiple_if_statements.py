a = int(input("Enter the age: "))

# If elif else ladder
if(a%2==0):
    print("a is even")
# End of If statement no: 1
    
# If statement no: 2
if(a>=18):
    print("You are above the consent")
    print("Good for you")

elif(a<0):
    print("You are entering an invalid age")    

elif(a==0):
    print("You are entering 0 which is not a valid age")
    
else:
    print("You are below the age consent")
# End of if statement no:2    

print("End of Program")    
