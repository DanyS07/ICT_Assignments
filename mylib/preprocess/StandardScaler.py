import numpy as np
def StandardScale(arr):
    arr=np.array(arr)
    y=(arr - np.mean(arr))/np.std(arr)
    return y
