import random
import string


str = input("Enter the string : ")
words = str.split(" ")
coding = input("1 for coding or 0 for decoding")
coding = True if (coding =='1') else False
print(coding) 
# we have to make coding = True when we ewant to encode

if(coding):
    nwords = [] # we have taken an empty list
    for word in words:
        if(len(str)>=3):
            r1 = ''.join(random.choices(string.ascii_lowercase, k=3))
            r2 = ''.join(random.choices(string.ascii_lowercase, k=3))

                
            stnew = r1 + word[1:] + word[0] + r2
            
            nwords.append(stnew)
        else:
            nwords.apend(word[::-1]) # otherwise append the reverse 
    print(" ".join(nwords)) # join ka kaam hota hai string + list             
    
else:
    nwords = [] # we have taken an empty list
    for word in words:
        if(len(str)>=3):
            stnew =word[3:-3] #starting ke 3 haracters hatane ke baad and last ke 3 characters hatane ke bad
            stnew = stnew[-1] + stnew[:-1] # last character + last-1 tak sare characters   
            nwords.append(stnew)
        else:
            nwords.apend(word[::-1])
    print(" ".join(nwords))    