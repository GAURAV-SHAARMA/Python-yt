# set ->> unordered collection of data items. they store multiple items into a single variable. seperated by coma nd inside {} . set are unchangeable , and do not contains multiple values


info = {'Gaurav' , 1, 2 , 4 ,5 , True  }
print(info)

s = {1 , 2 , 3  ,4, 2}
print(type(s)) #dont return 2 two times and order may be maintained may be not 

#empty set
harry = set()
print(type(harry))


#loop
for value in info:
    print(value)
    
    