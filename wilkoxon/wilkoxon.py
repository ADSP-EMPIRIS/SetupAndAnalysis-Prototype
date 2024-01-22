import numpy as np
from scipy.stats import wilcoxon

data1 = np.array([1, 2, 3, 4, 5, 6])
data2 = np.array([2, 3, 4, 5, 6, 7])

w, p = wilcoxon(data1, data2)

print(f"Wilcoxon test statistic: {w}")
print(f"P-value: {p}")
