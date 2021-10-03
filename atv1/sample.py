import math
import statistics
# import numpy as np
# import scipy.stats
# import pandas as pd

data_set = [5.2, 5.1, 4.9, 5.3, 5.7, 6.4, 8.4, 5.0, 4.9, 6.3, 5.7, 6.2, 8.2, 5.0, 8.2, 8.3, 8.9, 9.9, 5.7, 7.1, 7.0, 7.3, 5.5, 6.3, 4.7, 5.4, 5.4, 5.6, 6.0, 14.1];
data_set2 = [5.2, 6.4, 5.7, 8.3, 7.0, 5.4, 5.1, 8.4, 6.2, 8.9, 7.3, 5.4, 4.9, 5.0, 8.2, 9.9, 5.5, 5.6, 5.3, 4.9, 5.0, 5.7, 6.3, 6.0, 5.7, 6.3, 8.2, 7.1, 4.7, 14.1];
data_set3 = [5.2, 5.1, 4.9, 5.3, 5.7, 6.4, 8.4, 5.0, 4.9, 6.3, 5.7, 6.2, 8.2, 5.0, 8.2, 8.3, 8.9, 9.9, 5.7, 7.1, 7.0, 7.3, 5.5, 6.3, 4.7, 5.4, 5.4, 5.6, 6.0, 14.1]; 

# test if set is the same
data_set.sort()
data_set2.sort()
data_set3.sort()
print(data_set == data_set2)
print(data_set == data_set3)

# mean: average time for aplication load
print(f"Mean: {statistics.mean(data_set)}")
