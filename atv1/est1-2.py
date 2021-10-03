import math
import statistics
# import numpy as np
# import scipy.stats
# import pandas as pd

data_set = [5.2, 5.1, 4.9, 5.3, 5.7, 6.4, 8.4, 5.0, 4.9, 6.3, 5.7, 6.2, 8.2, 5.0, 8.2, 8.3, 8.9, 9.9, 5.7, 7.1, 7.0, 7.3, 5.5, 6.3, 4.7, 5.4, 5.4, 5.6, 6.0, 14.1]


# mean
print(f"Media: {statistics.mean(data_set)}")
print(f"Moda: {statistics.mode(data_set)}")
print(f"Mediana: {statistics.median(data_set)}")
print(f"Desvio Padrao Amostral: {statistics.stdev(data_set)}")