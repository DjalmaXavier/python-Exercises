import os
import time

def new_question():
  print("\nChoose the question, the options and the answer!")
  letters = ['A', 'B', 'C', 'D']
  question = {
    'Question' : None,
    'Options' : None,
    'Answer' : None,
  }
  question['Question']  = input('\nType the question: ')
  step2 = []
  for opt in range(4):
    option = input(f'\nOption {letters[opt]} = ')
    option_final = f'{letters[opt]} - {option}'
    step2.append(option_final)
  question['Options'] = step2
  answer = input("\nType the answer: ")
  aw_verification = len(answer) > 1
  aw_verification_digit = answer.isdigit()
  print(aw_verification_digit)
  print(aw_verification)
  if aw_verification or aw_verification_digit:
    while aw_verification or aw_verification_digit:
      answer = input("Type only one letter: ")
      aw_verification = len(answer) > 1
      aw_verification_digit = answer.isdigit()
  question['Answer'] = answer.upper()
  return question

questions_list = [
  {'Question' : 'What is 11 x 11?',
  'Options' : ['A - 100', 'B - 111', 'C - 121', 'D - 152'],
  'Answer' : 'C',
  },
  {
  'Question' : 'What is 20 divided by 5?',
  'Options' : ['A - 1', 'B - 4', 'C - 5', 'B - 6'],
  'Answer' : 'B',
  },
  {
  'Question' : 'What is 100 minus 45?',
  'Options' : ['A - 55', 'B - 60', 'C - 75', 'D - 45'],
  'Answer' : 'A',
  },
  {
  'Question' : 'What is 33 x 5?',
  'Options' : ['A - 149', 'B - 160', 'C - 165', 'D - 173'],
  'Answer' : 'C'
  }
]
score = 0
quant = len(questions_list)
num_question = 1
quant /= 2
print('-=-' * 15, "Math Quizz", '-=-'  * 15)
while True:
  for item in questions_list :
    question = item["Question"]
    options = item["Options"]
    answer = item["Answer"]
    print(f'\n{num_question} - {question}\n')
    for op in options:
      print(f'{op} ', end=' ')
    resp = input(f'\n\nAnswer: ')
    if resp.isalpha():
      resp_upper = resp.upper()
      if resp_upper == answer:
        print('\nCongrats, you hit!\n')
        print('-=-' * 34)
        score += 1
        num_question +=1
      else:
        print(f"\nWrong answer, the right answer is: {answer}\n")
        print('-=-' * 34)
        num_question +=1
    else:
      print("\nInvalid character, this test was invalidated.\n")
      break
  if score > quant:
    print(f"Congrats, you score {score} points!")
  elif score < quant:
    print(f"You dont get the medium. You score {score} points!")
  else:
    print(f'You get the medium. You score {score} points.\n')
  num_question = 1
  option = input ("\nDo you wanna do the quizz again?\n\n[Y]es or [N] = ").lower()
  option_y = option.startswith('y')
  option_n = option.startswith('n')
  if option_y:
    option = input("\nDo you wanna add a question on the quizz?\n"\
                    "\n[Y]es or [N] = ")
    option_y = option.startswith('y')
    option_n = option.startswith('n')
    if option_y:
      x = new_question()
      questions_list.append(x)
      print("\nQuestion add!\nGet ready...\n\n")
      print('-=-' * 34)
      score = 0
      continue
    elif option_n:
      score = 0
      continue
    else:
      print("\nInvalid option, closing..")
      time.sleep(2)
      break
  if option_n:
    print(f'\nThank you!\n')
    time.sleep(2)
    break
  else:
    print("\nInvalid option, closing..")
    time.sleep(2)
    break
os.system('cls')