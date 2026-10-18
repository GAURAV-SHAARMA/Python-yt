#DocString in python ->> these are the string literals that appears right after the defination of function , method  , class and modules

def square(n):
    '''Takes in a number n and returns the square if n'''
    #above one is docstring
    
    print(n**2)
square(5)
print(square.__doc__)# return that docString

#docstring change karne se program ka output change ho sakt ahia leking commment change karne per nhi 

# these are used to document the code used just after the defination of function , class , method

#docString will be none if it is not just afyter the defination of function , class , method 


#PEP 8 ->>>>
# it is document that provides guid;lines and best Practices to write python code ->> improve readability  , consistency of python code

# ->> Python enhancement proposal

#Zen of Python 
import this
#in terminal

# >>> import this
# The Zen of Python, by Tim Peters

# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.
# Flat is better than nested.
# Sparse is better than dense.
# Readability counts.
# Special cases aren't special enough to break the rules.
# Although practicality beats purity.
# Errors should never pass silently.
# Unless explicitly silenced.
# In the face of ambiguity, refuse the temptation to guess.
# There should be one-- and preferably only one --obvious way to do it.
# Although that way may not be obvious at first unless you're Dutch.
# Now is better than never.
# Although never is often better than *right* now.
# If the implementation is hard to explain, it's a bad idea.
# If the implementation is easy to explain, it may be a good idea.
# Namespaces are one honking great idea -- let's do more of those!
