#else in loop

for i in range(6):
    print(i)
    
    if i==4 :
        break
# now loop is breaked not finised now else will not get executed       
else:
    print("sorry no i")     
# now as there is an empty array so for loop will not run itwill go to else instead

# else is executed only when loop get successfully finished last stament get executed not breaked

#finished loop example 

i=0
while(i< 7):
    print(i)
    i+=1
        
else:
    print("not loop finished execute else")    