import estFunctions

dice1 = [1,2,3,4,5,6]
dice2 = [1,2,3,4,5,6]

omega = []

for side in dice1:
  for side2 in dice2:
    omega.append([side, side2])

print(f"Espaco Amostral:\n{omega}\nTotal de Elementos:\n{len(omega)}\n\n")
print("QUESTAO 5")
#--------------------------------------------------------------------------------------------------#
print("ITEM 1")
def resolver_5_1(): 
  primeiros_dados_filtrados = estFunctions.filtrar_dados_por_primeiro_valor([2,5], omega)
  print(f"primeiros_dados_filtrados por [2,5] ({len(primeiros_dados_filtrados)}): ", primeiros_dados_filtrados)

  soma_dos_dados_maior_ou_igual_a_sete = []
  for dados in omega:
    if dados[0] + dados[1] >= 7:
      soma_dos_dados_maior_ou_igual_a_sete.append(dados)
  print(f"soma_dos_dados_maior_ou_igual_a_sete({len(soma_dos_dados_maior_ou_igual_a_sete)}): ", soma_dos_dados_maior_ou_igual_a_sete)

  inter = estFunctions.conjunto_intersecao(primeiros_dados_filtrados, soma_dos_dados_maior_ou_igual_a_sete);
  print(f"Intersecao dos Eventos({len(inter)}): {inter}")

  print(f"Sao Independentes: {estFunctions.sao_independentes(primeiros_dados_filtrados, soma_dos_dados_maior_ou_igual_a_sete, omega)}")
resolver_5_1()

print("#--------------------------------------------------------------------------------------------------#")

print("ITEM 2")
def resolver_5_2(): 
  primeiros_dados_filtrados = estFunctions.filtrar_dados_por_primeiro_valor([2,5], omega)
  print(f"primeiros_dados_filtrados por [2,5] ({len(primeiros_dados_filtrados)}): ", primeiros_dados_filtrados)

  soma_dos_dados_menor_que_oito = []
  for dados in omega:
    if dados[0] + dados[1] < 8:
      soma_dos_dados_menor_que_oito.append(dados)
  print(f"soma_dos_dados_menor_que_oito({len(soma_dos_dados_menor_que_oito)}): ", soma_dos_dados_menor_que_oito)

  inter = estFunctions.conjunto_intersecao(primeiros_dados_filtrados, soma_dos_dados_menor_que_oito);
  print(f"Intersecao dos Eventos({len(inter)}): {inter}")

  print(f"Sao Independentes: {estFunctions.sao_independentes(primeiros_dados_filtrados, soma_dos_dados_menor_que_oito, omega)}")
resolver_5_2()

print("#--------------------------------------------------------------------------------------------------#")

print("ITEM 3")
def resolver_5_3(): 
  primeiros_dados_filtrados = estFunctions.filtrar_dados_por_primeiro_valor([1,3,4,6], omega)
  print(f"primeiros_dados_filtrados por [1,3,4,6] ({len(primeiros_dados_filtrados)}): ", primeiros_dados_filtrados)

  soma_dos_dados_maior_ou_igual_nove = []
  for dados in omega:
    if dados[0] + dados[1] >= 9:
      soma_dos_dados_maior_ou_igual_nove.append(dados)
  print(f"soma_dos_dados_maior_ou_igual_nove({len(soma_dos_dados_maior_ou_igual_nove)}): ", soma_dos_dados_maior_ou_igual_nove)

  inter = estFunctions.conjunto_intersecao(primeiros_dados_filtrados, soma_dos_dados_maior_ou_igual_nove);
  print(f"Intersecao dos Eventos({len(inter)}): {inter}")

  print(f"Sao Independentes: {estFunctions.sao_independentes(primeiros_dados_filtrados, soma_dos_dados_maior_ou_igual_nove, omega)}")
resolver_5_3()

print("#--------------------------------------------------------------------------------------------------#")

print("ITEM 4")
def resolver_5_4(): 
  primeiros_dados_filtrados = estFunctions.filtrar_dados_por_primeiro_valor([1,3,4,6], omega)
  print(f"primeiros_dados_filtrados por [1,3,4,6] ({len(primeiros_dados_filtrados)}): ", primeiros_dados_filtrados)

  soma_dos_dados_menor_que_dez = []
  for dados in omega:
    if dados[0] + dados[1] < 10:
      soma_dos_dados_menor_que_dez.append(dados)
  print(f"soma_dos_dados_menor_que_dez({len(soma_dos_dados_menor_que_dez)}): ", soma_dos_dados_menor_que_dez)

  inter = estFunctions.conjunto_intersecao(primeiros_dados_filtrados, soma_dos_dados_menor_que_dez);
  print(f"Intersecao dos Eventos({len(inter)}): {inter}")

  print(f"Sao Independentes: {estFunctions.sao_independentes(primeiros_dados_filtrados, soma_dos_dados_menor_que_dez, omega)}")
resolver_5_4()