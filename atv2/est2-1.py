def conjuntoComplementar(conjunto, espacoAmostral):
  resultado = []

  for el in espacoAmostral:
    if el not in conjunto:
      resultado.append(el)

  return resultado

def conjuntoUniao(conjuntoUm, conjuntoDois):
  return list(set(conjuntoUm + conjuntoDois))

def conjuntoIntersecao(conjuntoUm, conjuntoDois):
  resultado = []

  for el in conjuntoUm:
    if el in conjuntoDois:
      resultado.append(el)
  
  return resultado


# espaço amostral
omega = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# eventos
a = [2, 3, 4, 6, 8]
nonA = [1, 5, 7, 9, 10]

b = [1, 4, 5, 8, 10]
nonB = [2, 3, 6, 7, 9]

c = [2, 4, 5, 7, 9]
nonC = [1, 3, 6, 8, 10]

# 1 A
print(conjuntoIntersecao(conjuntoIntersecao(a, b), c))

# 1 B
print(conjuntoUniao(conjuntoUniao(nonA, b), c))

# 1 C
print(conjuntoIntersecao(conjuntoIntersecao(a, nonB), c))

# 1 D
print(conjuntoUniao(conjuntoUniao(nonA, nonB), c))

# 1 E
print(conjuntoIntersecao(conjuntoIntersecao(nonA, nonB), c))



# {4}
# {1, 2, 4, 5, 7, 8, 9, 10}
# {2}
# {1, 2, 3, 4, 5, 6, 7, 9, 10}
# {7, 9}