import fortran
import numpy as np
a = np.array([1, 2, 3], np.float32)
fortran.fmodule.fast_reverse(a, 2)
print(a)
