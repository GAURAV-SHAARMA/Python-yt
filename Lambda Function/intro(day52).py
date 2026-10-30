# In python lambda function is a small anonymous function without a name . it is defined using the lambda Keyword and has  a folowing syntax

# syntax->>>
# lambda arguments : expressions

#lambda function is often used in a situation where a small function is required for a short peiod of time. they are  commonly used as arguments for higher-order functions , such as map , filter , and reduce

#lambda function can include multiple statemnet



# def double(x):
#     return x*2

#uppper one is returning through function

#lower one is returning using lambda function
double = lambda x: x*2
cube = lambda x: x*x*x

#easily used when we have to pass function insde function
def appl(fun , val):
    return 6 + fun(val)
print(appl(cube ,2))
# below is same as above
print(appl(lambda x:x*x*x  , 2))

avg = lambda x , y , z : (x+y+z)/2

print(double(5))
print(cube(5))
print(avg(2 , 3 , 5))
