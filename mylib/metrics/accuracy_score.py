import numpy as np
def accuracy_score(arr_a,arr_b):
    arr_a=np.array(arr_a)
    arr_b=np.array(arr_b)
    score=np.sum(arr_a==arr_b)/len(arr_a)
    return(score)