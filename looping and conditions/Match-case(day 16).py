# Match - case statement ->>> it will comapre the given variable value to different shape also reffered as the pattern. The main idea is keep on comparing the variable with all the presemt patterns untills it fits into one

x = int(input("Enter the value of x: "))

match x:
    
    case 0: # here 0 is the value of x means when x = 0
        print("x is zero")
        
    case 1:
        print("x is 1")
        
    case 2:
        print("x is 2")
        
    case _ if x !=90:
        print(x , "is not 90")            
    case _ if x !=80:
        print(x , "is not 80")            
    case _ :
        print(x)            