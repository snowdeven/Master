import numpy as np
import multiprocessing as mp
import time

np.random.seed(1)

# Define the matrices
A = np.random.rand(5000, 5000)
B = np.random.rand(5000, 5000)


# Define the number of processes to use
# num_processes = mp.cpu_count()
num_processes = 9
# Divide the second matrix into equal parts
B_parts = np.array_split(B, num_processes, axis=1)

# Define a function to perform the matrix multiplication for each process
def matrix_multiplication(local_B):
    return np.dot(A, local_B)

if __name__ == '__main__':
    # Start the timer
    t0 = time.time()
    
    # Create a multiprocessing pool
    pool = mp.Pool(num_processes)
    
    # Map the matrix multiplication function to each part of the second matrix
    C_parts = pool.map(matrix_multiplication, B_parts)
    
    # Combine the results to form the resulting matrix
    C = np.hstack(C_parts)
    
    # Stop the timer
    t1 = time.time()
    
    # Print the time taken to perform the matrix multiplication
    print("Time taken:", t1-t0)