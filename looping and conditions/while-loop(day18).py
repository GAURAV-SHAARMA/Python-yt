# i=int(input("Enter the value of i:"))
# while(i< 30):
#     i =int(input("Enter the value of i:"))
#     print(i)
    
#     # this will take input till 29 above that lower print will get executed

# print("Done with the loop")


# count = 5
# while(count>0):
#     print(count)
#     count = count-1
# else:
#     print("I am inside else")    
    
# as soon as the value of while loop become false, the interpreter comes out of while loop and else will get executed    




# ->> do while using while Loop

# below code only give 0     
i = 0

while True:
    print(i)

    if i % 100 ==0:
        break

    i += 1
    


# >>>> This will print till 100    
    
i = 0

while True:
    print(i)

    if i % 100 == 0 and i != 0:
        break   
    i+=1
    
    
    
    
# . Without i != 0
# i = 0

# while True:
#     print(i)

#     if i % 100 == 0:
#         break

#     i += 1

# What happens:

# i starts with 0.
# while True starts an infinite loop.
# print(i) prints 0.
# Python checks i % 100 == 0.
# Since 0 % 100 = 0, the condition becomes True.
# Therefore, break executes immediately.
# The loop stops.

# Output:

# 0

# Summary:

# The loop stops at 0 because 0 is also divisible by 100. Therefore, the break condition becomes true in the very first iteration.

# 2. With i != 0
# i = 0

# while True:
#     print(i)

#     if i % 100 == 0 and i != 0:
#         break

#     i += 1

# What happens:

# Initially:

# i = 0

# The condition is:

# i % 100 == 0 and i != 0

# For i = 0:

# 0 % 100 == 0  → True
# 0 != 0        → False

# Because both conditions must be true when using and:

# True and False → False

# So break does not execute.

# Then:

# i += 1

# changes i from 0 to 1.

# The loop continues:

# 0
# 1
# 2
# 3
# 4
# ...

# When i = 100:

# 100 % 100 == 0 → True
# 100 != 0       → True

# Therefore:

# True and True → True

# So break executes and the loop stops.

# Output:

# 0
# 1
# 2
# 3
# ...
# 98
# 99
# 100
# Main concept to remember

# i % 100 == 0 checks whether i is divisible by 100. Since 0 is also divisible by every non-zero number, we add i != 0 to prevent the loop from stopping at the starting value 0.

# So:

# i % 100 == 0

# → stops at 0, 100, 200, 300...

# while:

# i % 100 == 0 and i != 0

# → stops at 100, 200, 300..., but not 0.    