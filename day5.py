# variables

# ->> container with store data
# ->> datatype ->> types of data use to declare variables


a = 1
print(a)
print(type(a))

Gaurav =9
b = Gaurav
print(b)

c = "Gaurav"
print(c)

d = 1
e = True
f = None
g = "gaurav"

print(type(f))


# to perform mathematical operations we have to take same type of datatypes

print(a+b) #->> work fine
# print(a+f) ->> will not work

x = complex(8 , 2)
print(type(x))


# Sequenced data

# ->> list ->>>

# it stores different type of datatypes
# It is mutable

list1 =[4 , 2.2 , [-1 , 2] , ["apple" , "banana"]]
print(list1)


# ->>>> Tuple->>>>
# ->> It is an ordered collection pf data with elements seperated by comma and enclosed within paranthesis
# ->> these are immutable

tuple= (("Parrot" , "Sparrow") ,("Lion" , " Tiger"))
print(tuple)




# ->>> dictionary ->> unordered collectio of data containing key : value pairs

dict = {
    'name':"Guarv",
    'age': 21,
    'number':1234567,
    "canvote":True
}
print(dict)

# ->>> In Python everything is Object



