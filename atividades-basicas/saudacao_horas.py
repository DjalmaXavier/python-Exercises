import sys

print("=" * 20, "Saudações", "=" * 20)
horas = input(f"\nFavor digitar as horas:  ")
minutos = input("\nAgora, digite os minutos:  ")
if len(horas) > 2 or len(minutos) > 2:
  print('\nHorário invalido!\n\nFinalizando programa.\n')
  sys.exit()
try:
    horasInt = int(horas)
    minutosInt = int(minutos)
    dia = horasInt >= 6 and horasInt <= 11 and \
          minutosInt >= 0 and minutosInt <= 59
    tarde = horasInt >= 12 and horasInt <= 18 and \
          minutosInt >= 0 and minutosInt <= 59
    noite = horasInt >= 19 and horasInt <= 23 and \
          minutosInt >= 0 and minutosInt <= 59
    madrugada = horasInt >= 0 and horasInt <= 5 and\
           minutosInt >=0 and minutosInt <= 59      
    if dia:
        print(f"\nBom dia, agora são {horas}:{minutos}\n")
    elif tarde:
        print(f"\nBoa tarde, agora são {horas}:{minutos}\n")
    elif noite:
        print(f"\nBoa noite, agora são {horas}:{minutos}\n")
    elif madrugada:
        print(f"\nBoa madrugada, agora são {horas}:{minutos}\n")
    else:
      print('\nHorário invalido!\n\nFinalizando programa...\n')
      sys.exit()
except ValueError:
    print(f"\nDigite apenas números, operação cancelada.\n")
