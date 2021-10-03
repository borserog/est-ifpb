import statistics

weight = [ 62, 75, 59, 56, 78 ]
height = [ 164, 180, 168, 162, 186 ]

# mean
print(f"Media Peso: {statistics.mean(weight)}")
print(f"Media Altura: {statistics.mean(height)}")

print(f"Desvio Padrao Amostral (Peso): {round(statistics.stdev(weight), 2)})")
print(f"Desvio Padrao Amostral (Altura): {round(statistics.stdev(height), 2)})")

print(f"Coeficiente de Variacao (Peso): {round((statistics.stdev(weight)/statistics.mean(weight)) * 100, 2)}%")
print(f"Coeficiente de Variacao (Altura): {round((statistics.stdev(height)/statistics.mean(height)) * 100, 2)}%")



