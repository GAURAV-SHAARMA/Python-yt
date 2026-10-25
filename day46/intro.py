#os module ->> it is a built-in library that provides the function for interacting with the operating system.

# It allows you to perform a wide variety of task  , such as reading and writing files , interacting with the file system and running system commands

import os

if(not os.path.exists("data")): #check if already exist or not
    os.mkdir("data") # // creates a director

for i in range(0 , 100):
    os.mkdir(f"data/day{i+1}")# create folders in dat folder
    
    #remane these folder
    