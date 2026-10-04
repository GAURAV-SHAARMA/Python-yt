# break statement ->>> it enables a program to skip over a part of code. it terminates the very loop it lies within 

for i in range(12):
    if(i==10):
        break # is loop ko chodkar nikal jao
    print("5 X " , i+1  , "=" , 5 * (i+1))
    
    
print("loop ko chodkar nikal gaya")    
    


# -->> continue ->>> iteration ko chodkar nika jao 

for i in range(12):
    if(i==10):
        print("skip the iteration")
        continue
    print("5 X " , i  , "=" , 5 * (i+1))
    
