import sys
print('=-' * 14, 'Validador de CPF', '-=' * 14)
cpf =input('\nDigite seu CPF: ')\
    .replace('.', '')\
    .replace('-', '')
sequencia_numerica = cpf == cpf[0] * len(cpf)
try:
    verificacao_letra = int(cpf)
except ValueError:
    print('\nPor favor, digite apenas números. Encerrando o programa...')
    sys.exit()
if sequencia_numerica :
    print('\nVocê digitou em sequencia! Encerrando o programa..')
    sys.exit()
elif len(cpf) > 11 or len(cpf) < 11:
    print('\nVocê não digitou a quantidade correta de números para um CPF.'\
          'Encerrando o programa..')
    sys.exit()
contador = 10
contador_d2 = 11
valores_cpf = cpf[:9]
primeiro_digito = 0
segundo_digito = 0
for i in valores_cpf :
    primeiro_digito += int(i) * contador
    contador -= 1
primeiro_digito = (primeiro_digito * 10) % 11
primeiro_digito = primeiro_digito if primeiro_digito < 9 else 0
valores_cpf_2 = valores_cpf + str(primeiro_digito)
for j in valores_cpf_2:
    segundo_digito += int(j) * contador_d2
    contador_d2 -= 1
segundo_digito = (segundo_digito * 10) % 11
segundo_digito = segundo_digito if segundo_digito <= 9 else 0
cpf_completo = valores_cpf_2 + str(segundo_digito)
if cpf_completo == cpf:
    print('\nSeu CPF é válido!')
else:
    print('\nSeu CPF não é valido!')