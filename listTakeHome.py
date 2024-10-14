fruits=['apple','banana','mango','orange']
fruits.append('grape')
fruits.insert(1,'kiwi')
fruits.remove('banana')
lastFruit=fruits.pop()
fruits.sort()
apple=fruits.count('apple')
fruits.reverse()
print(f"\nApple appears {apple} time.\n")
#final list and lastFruit
print(f"The final list is:\n{fruits}\nAnd the value of \nlast_fruit is {lastFruit}.")
