import statistics

age = [ 25, 21, 19, 18, 27, 22 ]
weight = [ 72, 65, 80, 72, 75, 74 ]
height = [ 175, 166, 182, 168, 171, 173 ]

# mean
print(f"Media Idade: {statistics.mean(age)}")
print(f"Media Peso: {statistics.mean(weight)}")
print(f"Media Altura: {statistics.mean(height)}")

print(f"Desvio Padrao Amostral (Idade): {round(statistics.stdev(age), 2)}")
print(f"Desvio Padrao Amostral (Peso): {round(statistics.stdev(weight), 2)}")
print(f"Desvio Padrao Amostral (Altura): {round(statistics.stdev(height), 2)}")

print(f"Coeficiente de Variacao (Idade): {round((statistics.stdev(age)/statistics.mean(age)) * 100, 2)}%")
print(f"Coeficiente de Variacao (Peso): {round((statistics.stdev(weight)/statistics.mean(weight)) * 100, 2)}%")
print(f"Coeficiente de Variacao (Altura): {round((statistics.stdev(height)/statistics.mean(height)) * 100, 2)}%")

