# importing in python is the process of loading code fro a python module into the current script. as well as additional module

import math as m
# from math import *
#>>> *(import all functions and variabbles from a module) it  is not recommended as it can lead to confusion and make it harder to understand where specific fucntion oe varible are coming from

from math import sqrt as s , pi

result1 = s(9) * pi
print(result1)

result = m.floor(4.1234)
print(result)
print(dir(m)) # returns all function used with math or any module
print(m.nan ,type(m.nan) )



#custom module
from module_Gaurav import welcome , Gaurav
welcome()
print(Gaurav)
    
    