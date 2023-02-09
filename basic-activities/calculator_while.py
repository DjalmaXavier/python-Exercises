#Simple calculator using While
while True:
  print('-=' * 8, 'Calculator 1.0','=-' * 8 )
  value_1 = input('\nEnter the first number: ')
  value_2 = input('Enter the second number: ')
  operation = input('Now, choose the operator [+, -, *, /]: ')

  try:
    value_1 = float(value_1)
    value_2 = float(value_2)
    if operation == '+':
      result = value_1 + value_2
      print(f'\nThe sum of {value_1} + {value_2} is = {result}\n')
    elif operation == '-':
      result = value_1 - value_2
      print(f'\nThe subtraction of {value_1} - {value_2} is = {result}\n')
    elif operation == '*':
      result = value_1 * value_2
      print(f'\nThe multiplication of {value_1} * {value_2} is = {result}\n')
    elif operation == '/':
      result = value_1 / value_2
      print(f'\nThe division of {value_1} / {value_2} is = {result}\n')
    else:
      print('\nPlease, enter a valid operator!\n')
      continue  
    option = input('Do you want to perform another operation?([Y]es or [N]o)?: ')
    option.lower()
    option_y = option.startswith('y')
    option_n = option.startswith('n')
    if option_y:
      print('\n')
    elif option_n:
      print("\nUntil the next time!")
      break
    else:
      print('\nYou entered an invalid option, the program will close..\n')
      break
  except:
    print('\nPlease, enter only valid values!\n')
    continue