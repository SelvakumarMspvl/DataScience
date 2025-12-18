import numpy as np

data  = np.genfromtxt('StudentDataCsv.csv', delimiter =',', skip_header = 1)
print(f"Length: {len(data)}\n")
print(f"Dimension: {data.ndim}\n")
print(f"Size: {data.size}\n")
print(f"Shape: {data.shape}\n")
print(f"Type: {data.dtype}\n")