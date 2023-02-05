sacola = []
print('=-' * 12, 'Sacola', '-=' * 12)
while True:
  item = input('\nDigite o item que deseja adicionar (ou aperte enter caso não'\
              ' queira adicionar nada): ')  
  if item != '':
    sacola.append(item)
    print(f'\nFoi adicionado o/a {item} na sua sacola.\n\nSua sacola possui ='\
          f' {sacola}\n')
  else:
    print(f'\nNenhum item foi adicionado!\n\nAté o momento, sua sacola possui ='\
         f' {sacola}\n')
  operacao = input(f'Gostaria de adicionar mais [+] itens, remover [-] ou'\
                   f' [F]inalizar?\n\nEscolha: ').lower()
  op_s = operacao.startswith('+')
  op_r = operacao.startswith('-')
  op_f = operacao.startswith('f')
  if op_s:
    continue
  elif op_r:
    while True:
      for item in range(len(sacola)):
        print(f'\n{item} - {sacola[item]}', end="")
        if sacola[item] == '':
          sacola.remove('')
      if len(sacola) == 0:
        print("\nNão há nada para remover!")
        break
      remover = input('\n\nDigite o número do item que deseja remover: ')
      try:
        remover = int(remover)
        for item in range(len(sacola)):
          if item == remover: 
            item_retirado = sacola.pop(item)
        print(f'\nO {item_retirado} foi removido com sucesso!\n')
      except ValueError:
        print('\nVocê digitou um valor invalido.')
        continue
      resposta = input(f'Gostaria de remover outro? [S]im/[N]ão: ').lower()
      resposta_s = resposta.startswith('s')
      resposta_n = resposta.startswith('n')
      if resposta_s:
        continue
      elif resposta_n:
        break
      else:
        print('\nCódigo digitado errado, você será redirecionado para o inicio..')
  elif op_f:
    sacola.sort()
    break
  else:
      print('\nCódigo digitado inválido, o programa será encerrado e a sacola'\
           ' será esvaziada...')
      sacola.clear()
      break
if len(sacola) == 0:
  print('\nSua sacola está vazia!')
else:
  print(f'\nSua sacola possui: ', end='')
  for item in range(len(sacola)):
    print(f'\n{item} - {sacola[item]} ', end="")