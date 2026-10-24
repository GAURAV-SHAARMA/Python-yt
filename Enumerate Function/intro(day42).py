# the Enumerate function is a built in function that allows loop over a sequence (such as list , tuple , or string) and get the index and value of each element in the sequence at the same time 


marks = [12 , 56 , 32 , 98 , 12 , 45 ,1 ,4]

# index=0
# for mark in marks:
#     print(mark)
#     if(index==3): #linter shows errorhere if we dont use index =0 in starting
#         print("Gaurav, Awesome")
#     index+=1    

# //enumerate function
for index , mark in enumerate(marks):
    print(index , mark)
    if(index==3):
        print("Awesome , Gaurav")


 
  
fruits = ['apple' , 'banana' , 'mango']
# for index , fruit in enumerate(fruits):
#     print(index , fruit)    
print('\n')    
    
    
    
# change the starting index
for index  , fruit in enumerate(fruits , start =1):
    print(index , fruit)
    