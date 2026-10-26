x = 4 #global 
print(x)

def Hello():
    global x
    x = 7
    y = 5 #local
    # local varibale destroy kar jate hai lekin global variable destro nhi hote
    
    print(f"the local x is {y}")
    print("Helow gaurav")

print(f"the global x is {x}")
Hello()    
print(f"the global x is {x}") # now we have defined a global x inside the function so that value of x will replace the previously defined global x outside the function

# print(y)   # this will cause error as y is local can be defined outside the function