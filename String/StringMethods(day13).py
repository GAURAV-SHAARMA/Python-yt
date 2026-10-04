
# string methods ->>>
# ->> Strings are immutable


a ="!Gaurav!!!!!!! !!!!! Gaurav"
print(len(a))
print(a.upper())
print(a.lower()) # this will create a bew string dont change the actual string
print(a.rstrip("!")) #trailing character ko remove

print(a.replace("Gaurav" , "Neha"))
# replace(old , new)

print(a.split(" "))
# this will create  a list with characters sepearrted by space

print(a.count("Gaurav"))
# count number of times Gaurav occures


blogHeading ="introduction tO jS"
print(blogHeading.capitalize())
# convert first character to uooer case and rest chaarcter to lower case


str1 = "Welcome to the console!!!"
print(len(str1))
print(str1.center(50))
# len of str1 is 25 so it addes 25 more space so that it will be move to center

print(str1.endswith("!"))
#give true or false 

print(str1.endswith("to" , 4 , 10))
# 4 se leke 9 tak kya str1 end ho rahi hai to se ?


str2 = "He's name is dan. He is an Honest man"
print(str2.find("is"))
# this will detact the first occurance of is (doesnt detect he'is)

print(str2.find("ishh")) # this will give -1 if not exist
# print(str2.index("ishh"))# this will end by giving an error if not exist

str3="WelcomeToConsole"
print(str3.isalnum())

#Alnum(alpha numeric charatcter) ->> it will return trueif entire string consist of A-Z , a-z , 0-9. If any other character or punctuations are present then it will return false

print(str3.islower())
print(str3.isprintable())
# return True if al characters are printable ond if there is any (\n) presnt in the string then it will return false
str4 =" "
print(str4.isspace())
print(str1.isspace())
# return true if onlyand only  white space is prenet in the string


str5 = "World Health Org"
print(str5.istitle()) 
# Return True if the string is a title-cased(first letter capital) string, False otherwise.

print(str5.startswith("World"))

print(str5.swapcase())
# lower case to upper and upeercse to lower case

str6 = "he is a good boy"
print(str6.title())
# convert all first letter to capita                                                                                    l

