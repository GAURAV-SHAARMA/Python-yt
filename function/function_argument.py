# def average(a , b):
#     print("the average is : " , (a+b)/2)
# average(4 , 6)  




# def average1(a=9 , b=1):
#     print("the average is : " , (a+b)/2)
# average1()  



# def average2(a=9 ,b= 1):
#     print("the average is : " , (a+b)/2)
# average2(1 ,5)  # now it will take later values not previously assigned values



# def average3(a , b=1):
#     print("the average is : " , (a+b)/2)
# average3(5)  # now b ki value vahi hogi previoulsy assigned 



# def average4(a=9 , b=1):
#     print("the average is : " , (a+b)/2)
# average4(b = 9)  # now b ki value  hogi newly  assigned 



# keyword argument

# average4(b = 9 , a=21)# order will be automatically chceked and arranged

#required argument ->> value deno hi deni hai 

# -->>> in case we dont pass the argument with a key = value syntax then it is necessary to pass the argument in the correct order and the number of argumnet pased shouldmatch the actual function defiunatiom 


#variable length argument->>>

def averageiterable(*numbers): # *numbers is taken as tuples((parameter) numbers: tuple[Unknown, ...])
    print(type(numbers))
    sum =0
    for i in numbers:
        sum = sum +i
    return sum / len(numbers)
        
c = averageiterable(5 ,6 , 7 , 1 , 8)  
print(c)      
  