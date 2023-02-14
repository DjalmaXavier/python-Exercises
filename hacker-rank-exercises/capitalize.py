# Complete the solve function below.
def solve(s):
  x = s.split(' ')
  new_word = ''
  for i in x:
    new_word += i.capitalize() + ' '
  return new_word

if __name__ == '__main__':
    s = input('Type the name: ')
    result = solve(s)
    print(result)