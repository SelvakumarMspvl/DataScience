import numpy as np

data  = np.genfromtxt('StudentDataCsv.csv', delimiter =',', skip_header = 1)
print(
        f"Length: {len(data)}\n"
        f"Dimension: {data.ndim}\n"
        f"Size: {data.size}\n"
        f"Shape: {data.shape}\n"
        f"Type: {data.dtype}\n"
)