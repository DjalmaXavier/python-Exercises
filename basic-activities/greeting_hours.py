import sys
'''
A program that will greet the user based on the time
'''
print("=" * 20, "Greetings", "=" * 20)
hours = input(f"\nPlease, enter the hours:  ")
minutes = input("\nNow, enter the minutes:  ")
if len(hours) > 2 or len(minutes) > 2:
  print('\nInvalid time!\n\nFinishing the program...\n')
  sys.exit()
try:
    hours_Int = int(hours)
    minutes_Int = int(minutes)
    morning = hours_Int >= 6 and hours_Int <= 11 and \
          minutes_Int >= 0 and minutes_Int <= 59
    afternoon = hours_Int >= 12 and hours_Int <= 18 and \
          minutes_Int >= 0 and minutes_Int <= 59
    night = hours_Int >= 19 and hours_Int <= 23 and \
          minutes_Int >= 0 and minutes_Int <= 59
    dawn = hours_Int >= 0 and hours_Int <= 5 and\
           minutes_Int >=0 and minutes_Int <= 59      
    if morning:
        print(f"\nGood morning, it's now {hours}:{minutes}\n")
    elif afternoon:
        print(f"\nGood afternoon, it's now {hours}:{minutes}\n")
    elif night:
        print(f"\nGood night, it's now {hours}:{minutes}\n")
    elif dawn:
        print(f"\nGood early hours, it's now {hours}:{minutes}\n")
    else:
      print('\nInvalid time!\n\nFinishing the program...\n')
      sys.exit()
except ValueError:
    print(f"\nEnter only numbers, please. Finishing the program...\n")
