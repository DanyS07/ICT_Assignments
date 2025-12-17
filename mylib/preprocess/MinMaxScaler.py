import numpy as np
def MinMaxScaler(arr):
    arr=np.array(arr)
    Min_val=np.min(arr)
    Max_val=np.max(arr)
    Scaled=(arr-Min_val)/(Max_val-Min_val)
    return Scaled
