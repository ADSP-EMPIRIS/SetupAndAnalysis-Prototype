import json
from os import read
from pdb import run
import numpy as np
from scipy.stats import wilcoxon, bootstrap

# ----- helper functions -----
def load_json_file(file_path):
    with open(file_path) as file:
        data = json.load(file)
    return data

def extract_data(data):
    reads = []
    deletes = []
    updates = []

    for data_dict in data['data']:
        reads.append(data_dict['read'])
        deletes.append(data_dict['delete'])
        updates.append(data_dict['update'])

    return reads, deletes, updates

# bootstrap
def mean_statistic(data):
    return np.mean(data)

# ----- path to dataset -----
data = load_json_file('testdata_1.json')
#data = load_json_file('testdata_2.json')

# ----- main -----

# split data into two benchmarking runs
run1 = data[0]
run2 = data[1]
# print("run1:")
# print(run1)
# print("\nrun2:")
# print(run2)

# ----- Bootstrapping -----
print("\nBootstrap for Benchmarking Run 1:\n")
reads, deletes, updates = extract_data(run1)

for metric in [reads, deletes, updates]:
    res = bootstrap((metric,), mean_statistic, vectorized=False, n_resamples=10000, confidence_level=0.99, method='percentile') # Nils: n=10.000, confidence_level=0.99
    print(f"Bootstrap Mean: {res.confidence_interval.low} - {res.confidence_interval.high}")

print("\nBootstrap for Benchmarking Run 2:\n")
reads, deletes, updates = extract_data(run2)

for metric in [reads, deletes, updates]:
    res = bootstrap((metric,), mean_statistic, vectorized=False, n_resamples=10000, confidence_level=0.95, method='percentile')
    print(f"Bootstrap Mean: {res.confidence_interval.low} - {res.confidence_interval.high}")

# ----- Wilcoxon -----
print("\nWilcoxon for Benchmarking Run 1:\n")
reads, deletes, updates = extract_data(run1)

for metric in [reads, deletes, updates]:
    w, p = wilcoxon(metric)
    print(f"Wilcoxon test statistic: {w}")
    print(f"P-value: {p}")

print("\nWilcoxon for Benchmarking Run 2:\n")
reads, deletes, updates = extract_data(run2)

for metric in [reads, deletes, updates]:
    w, p = wilcoxon(metric)
    print(f"Wilcoxon test statistic: {w}")
    print(f"P-value: {p}")