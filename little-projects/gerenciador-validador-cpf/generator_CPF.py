import random
print('=-' * 14, 'CPF Generator', '-=' * 14)
quantity = 0

for x in range(10): #Defines how many CPFs the user wants to generate
  
  cpf = ''

  #Add 9 numbers on CPF
  for num in range(9):
    cpf += str(random.randint(0, 9))

  quantity += 1
  count = 10
  count_second_digit = 11
  numbers_cpf = cpf[:9]
  first_digit = 0
  second_digit = 0

  #Math for the first digit
  for i in numbers_cpf : 
      first_digit += int(i) * count
      count -= 1
  first_digit = (first_digit * 10) % 11
  first_digit = first_digit if first_digit < 9 else 0
  valores_cpf_2 = numbers_cpf + str(first_digit)

 #Math for the second digit
  for j in valores_cpf_2: 
      second_digit += int(j) * count_second_digit
      count_second_digit -= 1
  second_digit = (second_digit * 10) % 11
  second_digit = second_digit if second_digit <= 9 else 0
  cpf_completo = valores_cpf_2 + str(second_digit)

  print(f'\nCPF {quantity} = {cpf_completo}')