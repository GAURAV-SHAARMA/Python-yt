# tuples are ordered collection of data items. they store multiple items in a single variable , tuples items are sperated by comma and enclosed within round brackets (). tuples are unchangeable 


tup = (1 ,2 , 76 , 342 , 32 , "green")
print(type(tup) , tup)

tup2 =(1 ,)# if we hve only one element then we have to add comma at last
# tup2[0]=5  not possible
print(type(tup2) , tup2)
print(tup[0])
print(tup[1])
print(tup[2])
print(tup[3])
print(tup[-1]) # tup[len(tup)-1]

if 342 in tup :
    print("yes")
else:
    print("no")    

tup3 = tup[1:4] # this slicing will create a new tuple no changes in already exiting one
print(tup3)


print(tup[:4])




