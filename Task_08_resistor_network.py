import numpy as np
import matplotlib.pyplot as plt

# Real-world case: Electrical resistor network
# Each node voltage is solved using Kirchhoff’s Current Law (KCL).
# The system Ax = b represents the balance of currents at each node.

A = np.array([
    [10., -2., -1.],
    [-2.,  9., -3.],
    [-1., -3.,  7.]
])

# Current injections at each node (Amps)
b = np.array([5., 0., -2.])

def jacobi(A, b, tol=1e-8, max_iter=500):
    D = np.diag(A)
    R = A - np.diagflat(D)
    x = np.zeros_like(b)
    errors = []
    for _ in range(max_iter):
        x_new = (b - R @ x) / D
        error = np.linalg.norm(x_new - x, ord=np.inf)
        errors.append(error)
        if error < tol:
            return x_new, errors
        x = x_new
    return x, errors

def gauss_seidel(A, b, tol=1e-8, max_iter=500):
    x = np.zeros_like(b)
    errors = []
    for _ in range(max_iter):
        old = x.copy()
        for i in range(len(b)):
            x[i] = (b[i] - A[i, :i] @ x[:i] - A[i, i+1:] @ old[i+1:]) / A[i, i]
        error = np.linalg.norm(x - old, ord=np.inf)
        errors.append(error)
        if error < tol:
            return x, errors
    return x, errors

# Run both iterative methods
x_j, err_j = jacobi(A, b)
x_gs, err_gs = gauss_seidel(A, b)

# Direct solution for comparison
x_exact = np.linalg.solve(A, b)

print("Jacobi node voltages:", x_j)
print("Gauss-Seidel node voltages:", x_gs)
print("Direct solution (exact voltages):", x_exact)

# Plot convergence
plt.semilogy(err_j, label="Jacobi")
plt.semilogy(err_gs, label="Gauss-Seidel")
plt.xlabel("Iteration")
plt.ylabel("Error (Infinity norm)")
plt.title("Convergence of iterative resistor network solution")
plt.legend()
plt.grid(True)
plt.show()
