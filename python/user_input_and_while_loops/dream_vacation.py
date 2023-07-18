#Poll program

responses = {}

polling_active = True

name = input("\nWhat is your name?")
response = input("\nWhat is your ideal dream vacation?")

responses[name] = response 

repeat = input("Would you like to let another person respond? (yes/no)")
if repeat == 'no' :
  polling_active = False 
  
print("\n --- Poll Results ---")

for name, response in responses.items():
 print(f"{name}'s dream vacation is {response}")
  