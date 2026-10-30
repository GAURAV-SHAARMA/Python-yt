#   REDUCE()
# ->>/ reduce(function , iterable)

#we have to import reduce 

from functools import reduce

numbers = [1 ,2 ,3 ,4,6 , 4 ,3]

sum = reduce(lambda x , y: x+y , numbers)

print(sum)