import numpy as np
from scipy.stats import bootstrap

data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

def mean_statistic(data):
    return np.mean(data)

res = bootstrap((data,), mean_statistic, vectorized=False, n_resamples=10000, confidence_level=0.95, method='percentile')

print(f"Bootstrap Mean: {res.confidence_interval.low} - {res.confidence_interval.high}")
