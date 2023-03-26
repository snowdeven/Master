from mpi4py import MPI
import numpy as np

# Initialiser MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
print(size)
# définir les matrices
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Diviser la deuxième matrice en parties égales
B_parts = np.array_split(B, size, axis=1)

# Distribuer les parties de la deuxième matrice à chaque processus
local_B = comm.scatter(B_parts, root=0)

# Effectuer la multiplication de matrices
local_C = np.dot(A, local_B)

# Collecter les résultats de chaque processus
C_parts = comm.gather(local_C, root=0)

# Combiner les résultats pour former la matrice résultante
if rank == 0:
    C = np.hstack(C_parts)
    print(C)