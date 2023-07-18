#List the sandwich orders and the finished sandwich orders.
sandwich_orders = ['ham & cheese','pastrami','meatball sub', 'pastrami','pizza calzone','pastrami', 'philly cheese steak','pastrami']

finished_sandwich = []

print("\nThe deli has ran out of pastrami")

#Remove any instances of 'pastrami' within the list.
while 'pastrami' in sandwich_orders:
  sandwich_orders.remove('pastrami')
  


#Loop through sandwich orders.
for sandwich in  sandwich_orders:
  sandwich = sandwich_orders.pop()
  print(f"Making the {sandwich.title()} order.")
  finished_sandwich.append(sandwich)


  
#Show all made sandwiches.
print("\nThe following sandwiches have been made:")
for sandwich in finished_sandwich:
  print(f"\nI have made your {sandwich.title()} sandwich.")
  
