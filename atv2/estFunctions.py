def conjunto_complementar(conjunto, espaco_amostral):
  resultado = []

  for el in espaco_amostral:
    if el not in conjunto:
      resultado.append(el)

  return resultado

def conjunto_uniao(conjunto_um, conjunto_dois):
  return list(set(conjunto_um + conjunto_dois))

def conjunto_intersecao(conjunto_um, conjunto_dois):
  resultado = []

  for el in conjunto_um:
    if el in conjunto_dois:
      resultado.append(el)
  
  return resultado

def sao_independentes(conjunto_a, conjunto_b, espaco_amostral):
  # calcula produto das probabilidades
  pa = len(conjunto_a)/len(espaco_amostral)
  pb = len(conjunto_b)/len(espaco_amostral)
  produto_pa_pb = pa*pb

  # probabilidade da intersecao
  a_inter_b = conjunto_intersecao(conjunto_a, conjunto_b)
  p_a_inter_b = len(a_inter_b)/len(espaco_amostral)

  print(f"P(A) = {pa}")
  print(f"P(B) = {pb}")
  print(f"P(A).P(B) = {pa*pb}")
  print(f"P(A & B) = {p_a_inter_b}")

  return produto_pa_pb == p_a_inter_b

def filtrar_dados_por_primeiro_valor(valores_desejaveis, espaco_amostral):
  return list(filter(lambda x: (x[0] in valores_desejaveis), espaco_amostral))
