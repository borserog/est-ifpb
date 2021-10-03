import math
import statistics
import numpy as np
# import scipy.stats
# import pandas as pd

defects = [
 [0] * 13,
 [1] * 11,
 [2] * 10,
 [3] * 9,
 [4] * 5,
 [5] * 2
]
data_set = [item for sublist in defects for item in sublist] 

# mean
print(f"Media: {statistics.mean(data_set)}")
print(f"Moda: {statistics.mode(data_set)}")
print(f"Mediana: {statistics.median(data_set)}")
print(f"Variância Amostral: {statistics.variance(data_set)}")