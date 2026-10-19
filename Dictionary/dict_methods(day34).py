ep1 = {
    122: 45 , 
    123 : 89  , 
    567:  69  , 
    679:  69
}
ep2={ 
     222: 67 , 
     566: 99
}
ep1.update(ep2)
print(ep1)

ep1.clear()
print(ep1) # empty dict

#empty dictionary
empt = {}
print(empt)

#pop
ep2.pop(222)
print(ep2)

#popitem ->> directly remove last item
ep3 = {
    122: 45 , 
    123 : 89  , 
    567:  69  , 
    679:  69
}
ep3.popitem()
print(ep3)

del ep3  #delete emtire dict
# print(ep3)

ep4 = {
     122: 45 , 
        123 : 89  , 
        567:  69  , 
        679:  69
}

del ep4[122] # now a particular key can be removed
print(ep4)
