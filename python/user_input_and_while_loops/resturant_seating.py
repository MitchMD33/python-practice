seating = input("Please enter the number of guests: ")
seating = int(seating)


if seating <= 8:
  print(f"\nTable for {seating} is available.")

else: 
  print("\nYou will need to wait for a table.")