multi = input("Enter a number, and I'll tell you if it's a multiple of 10 or not.: ")

multi = int(multi)

if multi %10 == 0:
  print(f"\nThe number {multi}, is a multiple of 10")

else:
  print(f"\nThe number {multi}, is not a multiple of 10")