'''
Verificar caractere repetido usando while
'''
frase = input('Digite uma frase: ').lower()
contador = 0
frequencia = 0
while contador < len(frase):
  letra_frase = frase[contador] #Pega a letra
  quantidade = frase.count(letra_frase) #Faz a contagem
  if letra_frase == ' ':
    contador += 1
    continue  
  elif quantidade > frequencia:
    frequencia = quantidade
    frequencia_let = letra_frase
  contador += 1
print(f'O/a "{frequencia_let}" apareceu {frequencia}x na frase.')