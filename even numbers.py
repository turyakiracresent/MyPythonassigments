num1 = int(input("Enter First number: "))
num2 = int(input('Enter Second number: '))

Sum= 0

for even in range(min(num1, num2), max(num1, num2) + 1, 2):
    print(even)
    Sum+= even

print("\nThe Sum of all even numbers within the range is :", Sum)
