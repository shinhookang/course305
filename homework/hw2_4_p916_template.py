import numpy as np 


# - - - - - TRUE SOLUTION - - - - - -
A = np.array([ [ 8, -2, -1, 0, 0],
               [-2, 9, -4, -1, 0],
               [-1, -3, 7, -1, -2],
               [0, -4, -2, 12, -5],
               [0, 0, -7, -3, -15]])

b = np.array([5, 2, 1, 1, 5])
x_sol = np.linalg.solve(A,b)
print('true sol = \n', x_sol)


# - - - - - PENTADIAG SOLUTION - - - - - -
def pentadiag(d,e,f,g,h,r):
    """
    pentadiag: solves a set of n linear algebraic equations
             with a tridiagonal-banded coefficient matris
    input:
    d = sub-subdiagonal vector of length n, first 2 elements = 0
    e = subdiagonal vector of length n, first element = 0
    f = diagonal vector of length n
    g = superdiagonal vector of length n, last element = 0
    h = super-superdiagonal vector of length n, last 2 elements = 0
    r = constant vector of length n
    output:
    x = solution vector of length n
    """
    n = len(f)
    x = np.zeros([n])

    # - - - - - - IMPLEMENTATION - - - - - - 

    # forward elimination

    # back substitution

    # - - - - - - IMPLEMENTATION - - - - - - 

    return x
    


n = 5
d = np.array(([0, 0, -1., -4., -7.]))
e = np.array(([0, -2., -3., -2., -3.]))
f = np.array(([8., 9., 7., 12., -15.]))
g = np.array(([-2., -4., -1., -5., 0]))
h = np.array(([-1., -1., -2., 0, 0]))
r = np.array(([5., 2., 1., 1., 5.]))

x = pentadiag(d,e,f,g,h,r)
print('pentadiag sol = \n', x)

err = np.linalg.norm(x - x_sol)
if err< 1e-12:
    print('Pass: err={}'.format(err))
else:
    print('Fail: err={}'.format(err))

 