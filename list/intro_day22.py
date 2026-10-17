# #list ->>>

# ordered collection of data items
 
# store multiple values in a single variable

# list ites are seperated by comma and enclosed within square bracket [].

# lists are changeable means we can alter them after creation


l = [3 , 4 ,5 , "Gaurav" ,True  ]

# print(l)
# print(type(l))

# print(l[0]) # list index(to access elements)
# print(l[1])
# print(l[2])
# print(l[3])
# print(l[4])

# print(l[-3]) #negative indexing(l[len(l)-3])
# print(l[len(l)-3]) #positive index

# if 7 in l:
#     print("yes")
# else:
#     print("no")    

# if "Gaurav" in l:
#     print("yes")
# else:
#     print("no")    
    
# if "aurav" in "Gaurav":
#     print("yes")
# else:
#     print("no")        


print(l[:])# print all elements in the list(l[0:len(l)])

print(l[1:])# print elements from 1 to last 

print(l[1:-1])# print from  to 4
print(l[1 :4:2]) # 2 referes to jump index it leaves 1 place and jump to next one(means we have to to remove 1 value and have to take 2nd value)


# List Comprehension 
# ->>>> these are used for creating new list from other iterables like lists  , tuples , dictionaries , sets and even in arrays and strings

lst = [i*i for i in range(4)]
print(lst)
lst = [i*i for i in range(10) if i%2 ==0]
print(lst)