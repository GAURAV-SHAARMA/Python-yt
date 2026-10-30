# in python the seek() and tell() function are used to work with file objects and their positions within a file. these functions are a part of the built-in io module


#seek()

# with open("my_file.txt", "r") as f:
#     print(type(f))

#     # Move to the 10th byte in the file
#     f.seek(10)

#     #tell() ->> it prints kahan tak hamne seek kiya hai ◘   (returns the current position in the file)
#     print(f.tell()) #10

#     # Read the ◘next 5 bytes
#     data = f.read(5)

#     print(data)


#trunctate ->>>>>

with open("my_file.txt" , "w") as f:
    f.write('hello World')
    f.truncate(5)  #size should be 5 characters
    
with open('my_file.txt' , 'r') as f:
    print(f.read())    
    
    


    