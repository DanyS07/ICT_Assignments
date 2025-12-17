import numpy as np

def mean_absolute_percentage_error(arr_x,arr_y):
    arr_x=np.array(arr_x)
    arr_y=np.array(arr_y)
    percentage_error=np.mean(np.abs(arr_x-arr_y))*100
    return percentage_error
