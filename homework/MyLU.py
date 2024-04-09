import numpy as np 
import scipy as sc


def LUfactor(A,tol=1e-8):
    """ LU factorization of an n by n matrix A
        A is factored to A = L * U

    Input: 
        A: n by n matrix
    Output:
        L: n by n lower triangular matrix
        U: n by n upper triangular matrix
    """

    m,n = A.shape
    if (m != n):
        print('Error: Matrix A should be squre! ')
        return 
    
    A = np.array(A)

    # - - - - - - - - - IMPLEMENTATION - - - - - - - 
    U = np.copy(A)
    L = np.diag(np.ones(n))
        
    for k in range(n):
        # check small pivot element
        if (np.abs(U[k,k]) < tol):
            print('Error: {0:d}th diagonal term is too small!'.format(k))

        # factor 
        L[k+1:,k]=U[k+1:,k]/U[k,k]

        # Gauss elimination
        # U[k,:] is the pivot equation
        for j in range(k+1,n):
            U[j,:] = U[j,:] - L[j,k] * U[k,:]


    # - - - - - - - - - IMPLEMENTATION - - - - - - -             

    return L, U



# TEST 
A = np.array([[3, -0.1, -0.2], [0.1, 7, -0.3], [0.3, -0.2, 10]])
b = np.array([0.3, -0.2, 10])

P,L,U = sc.linalg.lu(A)
print('Permutation Matrix =\n',P)
print('Lower Triangular Matrix =\n',L)
print('Upper Triangular Matrix =\n',U)

_L, _U = LUfactor(A)

if np.linalg.norm(L - _L) < 1e-12:
    print('PASS Lower Triangular matrix' )
else:
    print('FAIL Lower Triangular matrix!!' )

if np.linalg.norm(U - _U) < 1e-12:
    print('PASS Upper Triangular matrix' )
else:
    print('FAIL Uper Triangular matrix!!' )



