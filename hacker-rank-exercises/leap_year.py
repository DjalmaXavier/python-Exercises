def is_leap(year):
    leap = False
    divided_4 =  year % 4 == 0
    divided_100 = year % 100 == 0
    divided_400 = year % 400 == 0   
    if divided_4 and not divided_100:
      leap = True
    elif divided_100 and divided_400:
      leap = True
    else:
      leap = False
            
    return leap

year = int(input('Type the year: '))
print(is_leap(year))