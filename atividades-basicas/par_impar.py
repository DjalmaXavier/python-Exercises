import sys

print("=" * 20, "Par ou Impar", "=" * 20, '\n')

numInteiro = input(f"Favor digitar um número inteiro:  ")
try:
  inteiro = int(numInteiro)
  par = inteiro % 2 == 0
  if par:
      print(f"\nO número {inteiro} é par\n")
  else: 
      print(f"\nO número {inteiro} é impar\n")
except ValueError:
  print(f"\nVocê não digitou um número, operação cancelada.\n")
  sys.exit()