# a = int(input("Enter your age: "))
# print("Your age is :"  , a)

# # > , < , <= , >= , != , ==

# print(a>18)
# print(a>=18)
# print(a<=18)
# print(a==18)
# print(a!=18)

# if(a >18):
#     print("You can drive")
    
# else:
#     print("You cannot drive")
    
# print("ayyy!")        



applePrice = 10
budget = 200

if(budget - applePrice > 50):
    print("Alexa , add 1 kg Apple in the cart")

else:
    print("Alexa , do not add apple in the cart")    
    
    
    
# ->>>>elif statement->>>    

# num = int(input("Enter the Value :"))
# if(num < 0):
#     print("number is negative")
    
# elif(num == 0):
#     print("number is equal to zero")

# elif(num == 999):
#     print("Number is Special")
        
# else:
#     print("Number is positive")
           
# print("I am Happy now")           
            
            
            
# ->>>>>>>nested if Statement->>>            


num = int(input("Enter the Value :"))
if(num < 0):
    print("number is negative")
    
elif(num > 0):
    
    if(num<=10):
        print("number is between 1 - 10")
        
    elif(num > 10 and num <=20):
        print("number is between 11 to 20")
    
    else:
        print("Number is greater than 20")        
else:
    print("Number is zero")
           
print("I am Happy now")           
            
            