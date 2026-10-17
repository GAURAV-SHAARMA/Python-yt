l =[11 ,45 , 1 ,2 ,3 , 4 ,6]
print(l)

print(l.index(1))# return index of 1

l.append(7)
print(l)

l.sort()
print(l)

l.sort(reverse=True)
print(l)

l.reverse()
print(l)

print(l.count(1))

# copy method

m = l.copy()  
m[0] =0
print(l)
print(m)

#insert
l.insert(1 , 899) #(index , value update)
print(l)

#extend
n = [999 , 899 , 233]
l.extend(n) # n ke elements ko kholo and l ke end mai dal do(changes in l)
print(l)

#concatenation
k = l+n
print(k)