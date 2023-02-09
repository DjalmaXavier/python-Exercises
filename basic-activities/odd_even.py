import sys
'''
The good old odd or even
'''
print("=" * 20, "Odd or Even", "=" * 20, '\n')

number = input(f"Enter a number:  ")
try:
  num_int = int(number)
  even = num_int % 2 == 0
  if even:
      print(f"\nThe number {num_int} is even!")
  else: 
      print(f"\nThe number {num_int} is odd!")
except ValueError:
  print(f"\nYou don't enter a number... The program will be terminated")
  sys.exit()