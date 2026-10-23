#exception handling ->>> exception handling is the process of responding to unwanted or unexpected events when a computer program runs . exception handling deals with these to avovid program or system crash

# a = input("enter the number: ")
# print(f"multiplication table of {a} is : ")

# try:
#     for i in range(1 ,11):
#         print(f"{int(a)} X {i} =    {int(a)*i}")

# except:
#     print("Sorry some error occured")
    
# print("some imp lines of code")
# print("End of program")    


#like we dont use these try and except block we will get an error if user enter some string and by using this we can avoid the error




# handling specific type error

try:
    num = int(input("enter an integer: "))
    a = [6 , 3]
    print(a[num])
    
except ValueError:
    print("NUmber entered is not an integer")
    
except IndexError:
        print("Index Error!")
    
    
    
