#Calculadora simples usando While

while True:
  print('-=' * 8, 'Calculadora 1.0','=-' * 8 )
  valor_1 = input('\nDigite o numero desejado: ')
  valor_2 = input('Digite o segundo numero desejado: ')
  operacao = input('Digite a operação desejada [+, -, *, /]: ')

  try:
    valor_1 = float(valor_1)
    valor_2 = float(valor_2)
    if operacao == '+':
      resultado = valor_1 + valor_2
      print(f'\nA soma de {valor_1} + {valor_2} é = {resultado}\n')
    elif operacao == '-':
      resultado = valor_1 - valor_2
      print(f'\nA soma de {valor_1} - {valor_2} é = {resultado}\n')
    elif operacao == '*':
      resultado = valor_1 * valor_2
      print(f'\nA soma de {valor_1} * {valor_2} é = {resultado}\n')
    elif operacao == '/':
      resultado = valor_1 / valor_2
      print(f'\nA soma de {valor_1} / {valor_2} é = {resultado}\n')
    else:
      print('\nDigite um operador válido, tente novamente!\n')
      continue  
    opcao = input('Deseja realizar mais uma operação ([S]im ou [N]ão)?: ').lower()
    opcao_s = opcao.startswith('s')
    opcao_n = opcao.startswith('n')
    if opcao_s:
      print('\n')
    elif opcao_n:
      print("\nAté a próxima!\n")
      break
    else:
      print('\nVocê digitou uma opção inválida, o programa será fechado..\n')
      break
  except:
    print('\nDigite apenas valores válidos, tente novamente!\n')
    continue