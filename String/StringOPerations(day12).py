# String Operations->>

# 1. String Slicing
names = "gaurav,Sharma"
# print(len(names))

# print(names[0:6])
# this eill give character from 0 to 5(n-1)


fruit = "mango"
mangolen = len(fruit)
print(mangolen)
print(fruit[:4]) # 0-> 3(including 0 but not including 4)
print(fruit[1:4]) # 1-> 3
print(fruit[:]) # 0-> 4
print(fruit[:5]) # 0-> 4
print(fruit[0:-3]) # 0->1   
# print(fruit[0:len(fruit)-3])  = print(fruit[0:2])

print(fruit[-1:-3])#not print anything -> 4 -> 2 not possible

print(fruit[-3:-1]) #->> [len(fruit)-3:len(fruit)-1] -> 2-> 3


nm ="harry"
print(nm[-4:-2])