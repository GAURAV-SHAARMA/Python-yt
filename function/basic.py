# function ->> block of code that perform a specific task whenever it is called 

# a = 9
# b = 8
# # gmean = (a*b)/a+b
# # print(gmean)


# c= 8
# d= 7
# gmean2 = (c*d)/(c+d)
# print(gmean2)

def calculateGmean(a , b):
    mean = (a*b)/(a+b) 
    print(mean)
    
    
def isgreater(a ,b):
    if(a>b):
        print("a is greater")
    elif(a==b):
        print("both are equal")    
    else:
        print("b is greater")       

def islesser(a ,b):
    pass  
    #pass ->>> aage nikal jao ye code baad mai likhunga ye error nhi dega othrevise it will give error


a = int(input("enter value of a"))       
b = int(input("enter value of b"))       

isgreater(a , b)    
calculateGmean(a ,b)

