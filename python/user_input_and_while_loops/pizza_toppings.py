prompt = input("\nPlease enter the toppings you would like on your pizza:")
prompt += "\n(Enter 'quit' when you are finished.)"

while True:
    topping = input(prompt)
    
    if topping == 'quit':
      break
    
    else:
      print(f"We will add {topping.title()} to your pizza.")

