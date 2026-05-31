import numpy as np
a = np.array([
    [11,22,33],
    [44,55,66],
    [77,88,99]
])
print(a[:,0])           # first column
print(a[-1])            # last row
print(a[0:2,1:3])       # required part