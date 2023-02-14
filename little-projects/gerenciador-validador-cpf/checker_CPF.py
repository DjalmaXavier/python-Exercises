import sys
print('=-' * 14, 'CPF Validator', '-=' * 14)

cpf = input('Type your CPF: ')\
    .replace('.', '')\
    .replace('-', '')

numeric_sequence = cpf == cpf[0] * len(cpf)
try:
    verify_letter = int(cpf)
except ValueError:
    print('\nPlease, enter only numbers. Finish the program...')
    sys.exit()
if numeric_sequence :
    print('\nYou typed in sequence! Finish the program..')
    sys.exit()
elif len(cpf) > 11 or len(cpf) < 11:
    print('\nYou have not entered the correct number of numbers for a CPF.'\
          'Finish the program..')
    sys.exit()
count = 10
count_digit_2 = 11
cpf_numbers = cpf[:9]
first_digit = 0
second_digit = 0

#Validating the first digit
for i in cpf_numbers :
    first_digit += int(i) * count
    count -= 1
first_digit = (first_digit * 10) % 11
first_digit = first_digit if first_digit < 9 else 0
cpf_numbers_2 = cpf_numbers + str(first_digit)

#Validating the second digit
for j in cpf_numbers_2:
    second_digit += int(j) * count_digit_2
    count_digit_2 -= 1
second_digit = (second_digit * 10) % 11
second_digit = second_digit if second_digit <= 9 else 0
cpf_completo = cpf_numbers_2 + str(second_digit)

if cpf_completo == cpf:
    print('\nYour CPF is valid!\n')
else:
    print("\nYour CPF isn't valid!\n")