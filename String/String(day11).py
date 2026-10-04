# String ->> it is essentially a sequence or array of textual data enclosed in signle or may be double quoataion . Strings are used when working with unicode characters 

name= "Gaurav"
friend = "Anurit"
anotherFriend= 'Neha'

print("Hello , " + anotherFriend)

# apple = "He said , \"I want to eat an apple\""
# print(apple)


# multi line string should be enclosed in three quoataion ('''...''')
apple = '''He said , "I want to eat 
hi Gaurav
Hey i am good
an apple"'''

print(apple)


print(name[0]) # give first index of name character (G)
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[5])
# print(name[6])# thi will throw an error
print("\n")


#LOOPING through the string

print("Lets use a for loop\n")

for character in name:
    print(character)
    
for x in apple:
    print(x)    
    
# ->> loop -> blackbox which helps i traversing each element of string
    