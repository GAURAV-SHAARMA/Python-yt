import os

folders = os.listdir("data")

print(os.getcwd()) #return current directory
os.chdir("/python yt")
#direcory changed now lower program will not run

# print(folders)


for folder in folders:
    print(folder)
    print(os.listdir(f"data/{folder}"))# this will print all files inside yhe files also 

