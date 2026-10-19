# set mthods 

# 1. Joing of sets 

s1 = {1 , 2 , 5 ,6 }
s2 ={3 , 6 , 7}
print(s1.union(s2))
print(s1 , s2) #values didnt changed

s1.update(s2) #s1 ke ander wo values bhi le aao jo s2 mai hai
s2.update(s1) #s2 ke ander wo values bhi le aao jo s1 mai hai
print(s1 , s2) #s1  and s2 updated

#intersection ->> (common from both sets)
cities = {'Tokyo' , 'Madrid' , 'Berlin' , 'Delhi'}
cities2 = {'Tokyo' , 'Seol' , 'Kabul' , 'Madrid'}
print()
# cities3 = cities.intersection(cities2)
# print(cities3)
print(cities.intersection_update(cities2)) # jo dono mai common hogi wo aajayegi return hoke extra values hatt jayegi

# symmetric Diffference ->> print only items that are not similar to both sets

cities4 = {'Tokyo' , 'Madrid' , 'Berlin' , 'Delhi'}
cities5 = {'Tokyo' , 'Seol' , 'Kabul' , 'Madrid'}
print(cities4.difference(cities5)) # b-a
cities6 = cities4.symmetric_difference(cities5) # returns a new set 
print(cities6)



#there are several in-built methods 

# 1. isdisjoin() ->> checks if item of one set is present in another set returns false if items are present and return true if noot present

city = {'Tokyo' , 'Madrid' , 'Berlin' , 'Delhi'}
city2 = {'Tokyo' , 'Seol' , 'Kabul' , 'Madrid'}

print(city.isdisjoint(city2))


#2 . isuperset() -> checks if all items of a particular set is present in the original set , return true if all are prsent and false if not present

city4 = {'Tokyo' , 'Madrid' , 'Berlin' , 'Delhi'}
city3 = {'Tokyo' , 'Seol' , 'Kabul' , 'Madrid'}
print(city4.issuperset(city3))

#3 . issubset() ->  checksif all items of original set is present in the particular sett

set1 = { 1 , 2,3 , 4 ,5 }
set2 = { 1 , 2, 3 }
print(set2.issubset(set1))


#add
set1.add(7)
print(set1)

#remove
set1.remove(5) # if 5 will not present in set1 it will through an error
print(set1)

set1.discard(9) # but discard doent through any error
print(set1)


#pop ->> random value removal
item = set1.pop()
print(set1)
print(item) # 1 popped


#del ->> it is not a method rathher it is a keyword which delete the set entirely

del set2
# print(set2) ->> error

#clear 
# ->> clear all items from set and return empty set

set1.clear()
print(set1) #empty set
