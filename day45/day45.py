# if __name__== "__main__" in python 
# this idiom is a common pattern used in python script to determine wheather the script is being run directly or being imported as a module into another script


#__name__ this variable is a builtin- variable that is acutomaticaly set to the name of the current module. when a python script runs directly  , the __name__ variable is set to the string __main__ . when the script is imported as a module into another script then __name __ is set to the name of the module 


import Gaurav
# above one will execute thefunction in Gaurav.py

# Gaurav.welcome()
#this one to hum isko bol hi rahe hai execute hone ko 

# to total do baar same cheez print hogi ager hum Gaurav.welcome() ko hata bhi dete hai to import GAurav will execute the function once

# then we use if __name__ == "__main__" in Gaurav.py ab ye sirf ek baar execute hoga 

import Gaurav

Gaurav.welcome()


