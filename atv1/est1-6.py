import math
import statistics
import numpy as np
# import pandas as pd
# import scipy.stats

defects = [
 [(30+35)/2] * 2,
 [(35+40)/2] * 24,
 [(40+45)/2] * 30,
 [(45+50)/2] * 36,
 [(50+55)/2] * 40,
 [(55+60)/2] * 30,
 [(60+65)/2] * 16,
 [(65+70)/2] * 2,
]
data_set = [item for sublist in defects for item in sublist] 

# mean
print(f"Media: {statistics.mean(data_set)}")
print(f"Moda: {statistics.mode(data_set)}")
print(f"Mediana: {statistics.median(data_set)}")
print(f"Desvio Padrao Amostral: {statistics.stdev(data_set)}")
