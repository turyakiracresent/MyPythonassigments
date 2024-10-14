#user provides numbers
num1=int(input("Provide Your First Number: "))

num2=int(input("Provide Your Second Number: "))


num3=int(input("Provide Your Third Number: "))
#Performing comparisons
equalTo=num1==num2
notEqual=num2!=num3
greater=num3>num1
less=num1<num3
greaterThan=num2>=num3
lessThan=num3<=num1

#performing Logical Operations
And=num1<num2 and num1>num3 and num2<num3

Or=num1<num2 or num1>num3 or num2<num3

#outputing results
print("\n 'Performing Comparisons \n Using Logical Operators' \n")
print(f"Equal To = {equalTo}")
print(f"Not Equal = {notEqual}")
print(f"Greater = {greater}")
print(f"Less = {less}")
print(f"Greater Than = {greaterThan}")
print(f"Less Than = {lessThan}")

print("\n'Out Using \n Logical Operators'\n")
print(f"Logical And = {And}")
print(f"Logical Or = {Or}")
n=not num1<num2,not num3==num2
print(f"Logical Not is : {n}")
