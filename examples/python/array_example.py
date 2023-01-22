import numpy as np
import itertools

def np_average(vals):
        vals = np.array(vals)
        average_vals = np.average(vals)
        print(average_vals)

def np_sorted(vals):
        vals = np.array(vals)
        sorte_vals = sorted(enumerate(vals), key=lambda i: i[1])
        print(sorte_vals)

def iter_accumulate(vals):
        unique_items, counts = np.unique(vals, return_counts=True)
        print(unique_items)
        print(counts)

        percent = counts / len(vals)
        print(percent)

        accu = list(itertools.accumulate(percent))
        print(accu)

array = [4, 1, 3, 5, 4]

np_average(array)
np_sorted(array)
iter_accumulate(array)