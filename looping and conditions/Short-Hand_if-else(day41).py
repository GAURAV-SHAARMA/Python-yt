#if -else in one line ->> this is shorthand syntax used when the condition is being tested is simple and the code blocks to be executed are short 

a =  330333
b =  3303

# below one goes from left to right 
print("A") if a>b else print("=") if a==b else print("B")
print(9) if a> b else ""


c = 9 if a> b else 0
print(c)



# another example 

# result= value_if_true if condition else value_if_false
#same as ->> below one
# if condition:
#     result = value_if_true
# else:
#     result = value_if_false    