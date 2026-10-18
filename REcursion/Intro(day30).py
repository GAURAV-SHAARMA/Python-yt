# recursion is process of defining something in terms of itself

def fact(n):
    if n == 0:
        return 1
    elif n==1 :
        return 1
    else:
        return n * fact(n-1)
print(fact(6))   



def fibonacci(n):
    if n <= 1:
        return n 
    else:
        return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(3))    
    