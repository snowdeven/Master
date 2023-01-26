import numpy as np

############### PART-1 ###############

#------------ 1 ------------#
for i in range(10,0,-1):
    print(i)
    if i == 1:
        print("FINISH")

#------------ 2 ------------#
def printTicTacToe(board):
    for i in range(0,3):
        for j in range(0,3):
            if board[i][j] == 2:
                board[i][j] = "O"
            elif board[i][j] ==1:
                board[i][j] = "X"
            else:
                board[i][j] = " "
        print(board[i])
    
    

printTicTacToe([[0,0,1],[2,0,0],[0,0,0]])

############### PART-2 ###############
#------------ 1 ------------#
def fact(n):
    ans=1
    if n == 0 :
        return 1
    for i in range(1,n+1):
        ans = ans * i
    return ans


print(fact(0))
print(fact(4))



#------------ 2 ------------#
def converge_sum(n,tol):
    i=1
    sum_current =0
    sum_previous =0
    for i in range(1,n):

        sum_previous = sum_current
        sum_current += 1/fact(i)

        if abs(sum_previous - sum_current) < tol:
            print("Convergence reached above the tolerance condition :",)
            print(sum_current)
            break
        else:
            pass
    if abs(sum_previous - sum_current) > tol: 
        print(f"convergence no reached above the tolerance condition until {n} step")
        print(sum_current)
        

converge_sum(5,10**-4)

converge_sum(10,10**-4)

############### PART-3 ############### 
#------------ 1 ------------#
def is_prime(n):
        for i in range(2,n):
            if n % i == 0 :
                return False
                
        return True

for i in range(1,100):
    print(is_prime(i),i)


def factors_primes(n):    
    i = 2
    factors = []
    for i in range(2,n):
        if is_prime(i) == True:
            while n%i == 0:
                n //= i
                factors.append(i)
    if n > 1:
        factors.append(n)
    return factors
        

print(factors_primes(13013))

#------------ 2 ------------#
def sum_prime(n):
    return sum(set(factors_primes(n)))

print(sum_prime(13013))





