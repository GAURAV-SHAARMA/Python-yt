# "is" compares exact location of object in memory  and "==" compares the values of objects

# a =[1 , 2 ,3]
# b =[1 , 2 ,3]

a = 3
b = 3  #both pointing one memory location

print( a is b) # exact loaction of object in memory
print(a == b) #value


# 1. == (Equality Operator)
# Checks whether two variables have the same value.
# a = 10b = 10print(a == b)  # True



# Here, both variables contain the same value (10).
# 2. is (Identity Operator)
# Checks whether two variables refer to the same object in memory.
# a = [1, 2, 3]b = [1, 2, 3]print(a == b)  # Trueprint(a is b)  # False



# Why?
# - a == b → Both lists have the same values.
# - a is b → Both lists are separate objects in memory.