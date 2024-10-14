#getting the users names
firstName=input("Enter your first name: ")
lastName=input("Enter your last name: ")
fullName=firstName+" "+lastName
print(f"Your full name is: {fullName}")
print()

print(f"Hello,{fullName}! Welcome to the Python Series")
#getting users color
color=str(input("Input Your favorite color: "))
#use .upper() to convert to upper case and others accordingly
print(f"UpperCase is: {color.upper()}")
print(f"LowerCase is: {color.lower()}")
#to get string lenth use:  len(VariableName)
length=len(color)
print(f"The length of the color string is: {length} characters")
print(f"Your name is {fullName} and favorite color has {length} characters")