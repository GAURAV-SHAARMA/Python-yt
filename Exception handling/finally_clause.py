# the finally code block is also a part of exception handling . when we handle exception using try and except block , we can include a finally at the end. the finally block is always executed . so it is genarally used for concluding tasks like closing the file resouces or closing database conection 

def funct1():
    try :
        l = [1 , 5 , 6, 7]
        i = int(input("enter the index: "))
        print(l[i])
        return 1
    except:
        print("some error occured")
        return 0
    
    finally:
        print("I am always executed")  
    # now the situation comes up why we cant use normal print function that will also executed everytime 
    # so when we wrap this entire in a function then the only print will not get executed nut the finally wala will get executed
    # print("I am executed")          

x = funct1()    
print(x)