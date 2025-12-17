import numpy as np
def mean_squared_error(arr1, arr2):
    arr1=np.array(arr1)
    arr2=np.array(arr2)
    error=(np.mean((arr1 - arr2)**2))
    return error