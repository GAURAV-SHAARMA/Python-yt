# def cube(x):
#     return x*x*x
# print(cube(3))


#returing cube of each item in the list and append in the nwe list
# l = [1 , 2 ,4 , 6 , 4, 3]
# newl =[]
# for item in l:
#     newl.append(cube(item))
# print(newl)    



# map , filter  , reduce ->> these functions are built-in function that allows you to apply a function to a sequence of elements and return a new sequence. These functions are known as the higher order functions , as they take other functions as argument


#using MAP
# ->> map(function , iterable(like list jispe function apply karna hai))

l = [1 ,2 ,3 ,4,6 , 4 ,3]
newl = list(map(lambda x: x*x*x, l))
print(newl)



#using FILTER
#->>> filter(pedicate(filter_function) , iterable)

def filter_function(a):
    return a > 4 
    # if above true return true else false
newnewl = list(filter(filter_function , l))
print(newnewl) # return only [6]


#   REDUCE()
# ->>/ reduce(function , iterable)