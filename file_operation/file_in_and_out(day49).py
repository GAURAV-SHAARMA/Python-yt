#opening a file 



#reading a file 

# # f = open('my_file.txt' , 'r') #("file name" , "operation- read , write ")
# f = open('my_file.txt') #("file name" , "operation- read , write ") # read mode is default

# text = f.read() # same mode will be used like f include 'r' then text should also inlcude read
# print(text)
# f.close()





# modes in file 
# read  , write , append(a) , create(x) , text(t) , binary(b)


#writing a file
# writing to a file will override its content

# f = open("my_file.txt" , "w")
# f.write("Hellow world!")
# f.close()


#appending
# f = open("my_file.txt" , "a")
# f.write("Hellow world!")
# f.close()

# it is important to close the file after you aredone with it
with open('my_file.txt' , 'a') as f:
    f.write("Hey I am inside with")

# now there is no need to close the file it will automatically do it
