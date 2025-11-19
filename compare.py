import numpy as np
from vectors import Vector

v1 = Vector([1,2,3])
v2 = Vector([4,5,6])

# compare with numpy
print("My dot:", v1.dot(v2))
print("Numpy dot:", np.dot(np.array([1,2,3]), np.array([4,5,6])))
