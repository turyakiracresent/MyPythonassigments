#nested if
age = int(input("Enter your age: "))
if age >= 18:
    print("You are an Adult.")
    country = input("Input your Nationality: ")
    if country == "Ugandan":
        print("You are eligible to vote\n in Uganda")
    else:
        print("You are not eligible to vote in Uganda")
        
else:
    
    print("You cannot vote Since\n 'You Are Not An Adult' ")
