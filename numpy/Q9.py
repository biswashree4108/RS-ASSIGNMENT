import numpy as np
a = np.array([
    [1,2,3]
])
print("dtype:", a.dtype)        #datatype
b = a.astype(float)             #change datatype
print(b.dtype)                  #datatype


#dtype shows the datatype of the array elements.
#astype() is used to change the datatype of the array elements. 