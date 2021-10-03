dice1 = [1,2,3,4,5,6]
dice2 = [1,2,3,4,5,6]

omega = []

for side in dice1:
  for side2 in dice2:
    omega.append([side, side2])

print(f"Espaco Amostral:\n{omega}\nTotal de Elementos:\n{len(omega)}\n\n")

#--------------------------------------------------------------------------------------------------#
somaImpar = []
primeiroDadoMenorQueDois = []

for tuple in omega:
  sum = tuple[0] + tuple[1]
  if (sum % 2 != 0):
    somaImpar.append(tuple)

for tuple in omega:
  if tuple[0] < 2:
    primeiroDadoMenorQueDois.append(tuple)

somaImparEPrimeiroDadoMenorQueDois = []

for tuple in somaImpar:
  for tuple2 in primeiroDadoMenorQueDois:
    if tuple == tuple2:
      somaImparEPrimeiroDadoMenorQueDois.append(tuple2)

print("QUESTAO 4A")
print(f"somaImpar {somaImpar}")
print(f"primeiroDadoMenorQueDois {primeiroDadoMenorQueDois}")
print(f"somaImparEPrimeiroDadoMenorQueDois {somaImparEPrimeiroDadoMenorQueDois}")
print(f"Probabilidade de soma impar COM primeiro dado menor que dois:\n{len(somaImparEPrimeiroDadoMenorQueDois)/len(primeiroDadoMenorQueDois)}")

#--------------------------------------------------------------------------------------------------#
primeiroDadoMaiorQueQuatro = []
somaDosDadosPar = []
primeiroDadoMaiorQueQuatroESomaDosDadosPar = []

for tuple in omega:
  if tuple[0] > 4:
    primeiroDadoMaiorQueQuatro.append(tuple)

for tuple in omega:
  if ((tuple[0] + tuple[1]) % 2 == 0):
    somaDosDadosPar.append(tuple) 

for tuple in primeiroDadoMaiorQueQuatro:
  for tuple2 in somaDosDadosPar:
    if (tuple == tuple2):
      primeiroDadoMaiorQueQuatroESomaDosDadosPar.append(tuple2)

print("\n\nQUESTAO 4B")
print(f"primeiroDadoMaiorQueQuatro: {primeiroDadoMaiorQueQuatro}")
print(f"somaDosDadosPar: {somaDosDadosPar}")
print(f"primeiroDadoMaiorQueQuatroESomaDosDadosPar({len(primeiroDadoMaiorQueQuatroESomaDosDadosPar)}): {primeiroDadoMaiorQueQuatroESomaDosDadosPar}")
print(f"probabilidade primeiro dado maior que quatro e soma dos dados par: {len(primeiroDadoMaiorQueQuatroESomaDosDadosPar)/len(omega)}")

#--------------------------------------------------------------------------------------------------#

primeiroDadoMenorQueQuatro = []
somaImpar2 = []
primeiroDadoMenorQueQuatroESomaImpar = []

for tuple in omega:
  if tuple[0] < 4:
    primeiroDadoMenorQueQuatro.append(tuple)

for tuple in omega:
  sum = tuple[0] + tuple[1]
  if (sum % 2 != 0):
    somaImpar2.append(tuple)

for tuple in somaImpar2:
  for tuple2 in primeiroDadoMenorQueQuatro:
    if tuple == tuple2:
      primeiroDadoMenorQueQuatroESomaImpar.append(tuple2)

print("\n\nQUESTAO 4C")
print(f"somaImpar({len(somaImpar2)}): {somaImpar2}")
print(f"primeiroDadoMenorQueQuatro({len(primeiroDadoMenorQueQuatro)}): {primeiroDadoMenorQueQuatro}")
print(f"primeiroDadoMenorQueQuatroESomaImpar({len(primeiroDadoMenorQueQuatroESomaImpar)}): {primeiroDadoMenorQueQuatroESomaImpar}")
print(f"Probabilidade de primeiro dado menor que quatro COM com soma impar:\n{len(primeiroDadoMenorQueQuatroESomaImpar)/len(somaImpar2)}")

#--------------------------------------------------------------------------------------------------#



#--------------------------------------------------------------------------------------------------#



#--------------------------------------------------------------------------------------------------#
