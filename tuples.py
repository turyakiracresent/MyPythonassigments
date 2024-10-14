name=('Simon','John','TK','John')
#print(name) prints a tuple
# accessing a tuple by its index
#print(name[2])
print(name.count('John')) #counts the no of times john appears apear 
#print(name.index('John')) returns first occurrence in a tuple
#Tuple with multiple elements
person=('John',78,"Computer Scientist","MarrieCouple","Catholic","Faithfull")
#un packing a tuple
name,age,*profession=person
print(name)
print(age)
print(profession)