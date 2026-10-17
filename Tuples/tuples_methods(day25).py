#manipulating tuples 
# -->>> tuple are immutable  , hence if you want to add  , remove  , change tuple item , then you first must convert the tuple into a list , then perform operations on that list and then list to tuple conversion



# Tuples are immutable, so we cannot directly add, remove, or change items.

countries = ("Spain", "Italy", "India", "England", "Germany")  # Tuple

temp = list(countries)  # Convert tuple into a list

# Perform operations on the list
temp.append("Russia")   # Add an item at the end
temp.pop(3)             # Remove the item at index 3 ("England")
temp[2] = "Finland"     # Change the item at index 2 ("India")

countries = tuple(temp)  # Convert list back into a tuple

print(countries)



#concatenation ->>> directly can be performed without any conversion

countries1 = ("pak" , "afgan" , "shri lanka" , "bang")
countries2 =("vietnam" ,"India" , "china")

southEastAsia = countries1 + countries2

print(southEastAsia)


# count method
tuple1 =(1 ,2 ,3  , 2 , 3 , 1 , 2 , 3)
res = tuple1.count(3)
print("count of 3 in tuple1 is :" , res)

#index method
# ->> returns the first occurance of the given element fromthe tuple 

print(tuple1.index(3 ,4 ,8  ))
#(element(to find) , start , end(slicing))

print(len(tuple1))