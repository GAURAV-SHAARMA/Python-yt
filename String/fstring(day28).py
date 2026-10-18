#fstring ->>>  new string formatting introduced by the PEP 498 
# It is also known as formatted string literals. It is a way to embed expressions inside string literals, using curly braces {}. The expressions are evaluated at runtime and then formatted using the format() protocol.

# It is formatted in much same way as the str.format() method


#old string formating
# letter = "Hey my name is {0} and I am from {1}"

# name = "Guarav"
# country = "India"

# print(letter.format(name , country))



# fstring ->>>>>>>>>.......

country = "India"
name ="Gaurav"

print(f"We use f-String like this : Hey my name is {name} and I am from {country}")

print(f"We use f-String literals like this : Hey my name is {{name}} and I am from {{country}}")



#.2f ->>>>>>>.....

#old string format
txt = "for only {price:.2f} dollars!" #.2f means it will take value only till two deciaml
print(txt.format(price=49.09999))

#new fstring->>>>>
price=49.09999
txt1=f"for only {price:.2f} dollars!"
print(txt1)


print(type(f"{2*30}")) #return in form of string


