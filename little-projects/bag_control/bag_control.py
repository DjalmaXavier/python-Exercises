bag = []
print('=-' * 12, 'Personal Bag', '-=' * 12)
while True:
  item = input("\nEnter the item you want to add (or press enter if you don't"\
              " want add anything): ")  
  if item != '':
    bag.append(item)
    print(f'\nThe {item} was add to your bag.\n\nYour bag has ='\
          f' {bag}\n')
  else:
    print(f'\nNo items have been added!\n\nSo far, your bag has ='\
         f' {bag}\n')
  operacao = input(f'Do you like to add [M]ore itens, [R]emove or'\
                   f' [F]inish?\n\nOption: ').lower()
  op_m = operacao.startswith('m')
  op_r = operacao.startswith('r')
  op_f = operacao.startswith('f')
  if op_m:
    continue
  elif op_r:
    while True:
      for item in range(len(bag)):
        print(f'\n{item + 1} - {bag[item]}', end="")
        if bag[item] == '':
          bag.remove('')
      if len(bag) == 0:
        print("\nTheres nothing to remove!")
        break
      remove = input('\n\nEnter the number of the item do you want to remove: ')
      try:
        remove = int(remove)
        for item in range(len(bag)):
          if item + 1 == remove: 
            remove_item = bag.pop(item)
        print(f'\nThe {remove_item} has been removed!\n')
      except ValueError:
        print('\nYou have entered an invalid number.')
        continue
      option = input(f'Would you like to remove another one? [Y]es/[N]o: ').lower()
      option_Y = option.startswith('y')
      option_N = option.startswith('n')
      if option_Y:
        continue
      elif option_N:
        break
      else:
        print('\nInvalid code.\n\nYou will be redirected to the remove page..')
        continue
  elif op_f:
    bag.sort()
    break
  else:
      print('\nInvalid code\n\nThe program will end, and the bag will be emptied')
      bag.clear()
      break
if len(bag) == 0:
  print('\nYour bag is empty!')
else:
  print(f'\nYour bag has: ', end='')
  for item in range(len(bag)):
    print(f'\n{item + 1} - {bag[item]} ', end="")