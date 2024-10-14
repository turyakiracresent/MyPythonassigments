total= 0
while True:
        num = int(input("Enter a number: "))
        if num < 0:
            break
        total+= num
print(f"The Sum of the numbers entered is : {total}")
