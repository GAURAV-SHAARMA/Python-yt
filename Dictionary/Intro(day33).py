#dictionary ->>>>  ordered collection of data items. they can store multiple items into a single variable. Dict items are key-value paired that are seprated by comma and enclosed into {}

dic ={
    "gaurav":"Human being",
    "spoon" : "Object",
     567: 'neha',
     678: 'zakir',
     56: 'subham',
     67: 'ankit'
 
}

# print(dic["gaurav1"]) # it will through error as it is not present in dic

print(dic.get('gaurav1')) # here still gaurav1 is not present in dic but it is giving none in place of error
print(dic[567]) # this will return the value corressponding to a particular key given
print(dic)  
print(dic.keys()) # it will return all keys

for key in dic.keys():
    print(f"the value corresponding to the key {key} is {dic[key]}") 

print(dic.values()) 
 
 
print(dic.items())
for key , value in dic.items():
    print(f"the value corresponding to the key {key} is {value}")