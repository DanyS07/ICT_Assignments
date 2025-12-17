
import numpy as np

def mean_absolute_error(arr1, arr2):
    arr1 = np.array(arr1)
    arr2 = np.array(arr2)
    X = np.mean(np.abs(arr1 - arr2))
    return X
