age = input("\n Welcome to ABC movie theater, please enter your age: ")
age = int(age)
  
  
if age < 3:
  print("The ticket is free.")

elif age >=3 and age <= 12:
  print("The ticket is $10")
  
elif age > 12:
  print("The ticket will cost $15 dollars.")
    