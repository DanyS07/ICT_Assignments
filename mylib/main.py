from preprocess.MinMaxScaler import MinMaxScaler
from preprocess.StandardScaler import StandardScale
from metrics.accuracy_score import accuracy_score
from metrics.mean_absolute_error import mean_absolute_error
from metrics.mean_absolute_percentage_error import mean_absolute_percentage_error
from metrics.mean_squared_error import mean_squared_error

a=[1,2,3,4,5]
arr_a=[1,0,1,1]
arr_b=[1,0,0,1]

z=accuracy_score(arr_a,arr_b)
x=MinMaxScaler(a)
y=StandardScale(a)
k=mean_absolute_error(arr_a, arr_b)
p=mean_absolute_percentage_error(arr_a, arr_b)
q=mean_squared_error(arr_a,arr_b)
print(f"MinMaxScaler:{x}")
print(f"StandardScale:{y}")
print(f"Accuracy score:{z}")
print(f"Mean Absolute error:{k}")
print(f"Mean Absolute Percentage error:{p}")
print(f"Mean Squared error:{q}")

