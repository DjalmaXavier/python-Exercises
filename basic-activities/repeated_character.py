'''
Program that counts the frequency of x characters in a sentence
'''
sentence = input('Enter a sentence: ').lower()
count = 0
frequency = 0
while count < len(sentence):
  letter_sentence = sentence[count] #Pega a letra
  quantity = sentence.count(letter_sentence) #Faz a contagem
  if letter_sentence == ' ':
    count += 1
    continue  
  elif quantity > frequency:
    frequency = quantity
    frequencia_let = letter_sentence
  count += 1
try:
  print(f'\nThe "{frequencia_let}" appeared {frequency} times on the sentence.')
except NameError:
  print("\nYou have not entered any letters. The program will end... ")