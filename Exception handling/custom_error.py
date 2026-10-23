# In python we can raise a custom error by using the raise keyword

a = int(input("Enter any value between 5 and 9: "))

if(a<5 or a>9):
    quit() # now by using this the program will not reach to the custom error
    #custom error
    raise ValueError("value should be between 5 and 9")


# we can handle the eception by creating a new class that is derived from the built0-in exception class

# class CustomException(Exception):
#     #code
#     pass
# try:
#     #code
    
# except CustomException:
#     #code
        
        
        