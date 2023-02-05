import random
print('=-' * 14, 'Gerador de CPF', '-=' * 14)
quantidade = 0
for x in range(10):
  cpf = ''
  for num in range(9):
    cpf += str(random.randint(0, 9))
  quantidade += 1
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
  print(f'\nCPF {quantidade} = {cpf_completo}')