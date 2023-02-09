import os
'''
Program where the user will guess the secret word (variable secret)
'''
secret = 'Github'.lower()
hits = '' 
attempts = 0
errors = 0
print('=-' * 12, 'Secret Word', '-=' * 12)
print('\nGuess the secret word to end the loop!')
while True:
  word_complete = ''
  letter = input('\nTry to guess a letter: ').lower()
  if len(letter) > 1:
    print('\nType just one letter!')
    continue
  elif letter.isalpha() is False:
    print('\nType just letters!')
    continue
  if letter in secret:
    hits += letter
    for i in secret:
        if i in hits:
          word_complete += i
        else:
          word_complete += '*'
    print(f'\nYou find the letter "{letter}" of the word: {word_complete}')
    attempts += 1
  else:
    print(f'\nA letter "{letter}" is not in the word: {word_complete}')
    attempts += 1
    errors += 1
    continue
  if word_complete == secret:
    os.system('cls')
    print(f"Congrats! You discover the word: {secret}\n"\
          f'\nYou need a total of {attempts} tries and {errors} errors')
    break