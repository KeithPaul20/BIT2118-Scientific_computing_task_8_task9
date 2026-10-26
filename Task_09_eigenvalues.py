import numpy as np 
# Adjacency matrix for a small undirected network. 
# Node order: A, B, C, D 
A = np.array([ 
[0., 1., 1., 0.], 
[1., 0., 1., 1.], 
[1., 1., 0., 1.], 
[0., 1., 1., 0.] 
]) 
eigenvalues, eigenvectors = np.linalg.eig(A) 

# Dominant eigenvalue/eigenvector 
index = np.argmax(np.real(eigenvalues)) 
dominant_value = np.real(eigenvalues[index]) 
dominant_vector = np.abs(np.real(eigenvectors[:, index])) 
centrality = dominant_vector / dominant_vector.sum() 
nodes = ["A", "B", "C", "D"] 
print("Dominant eigenvalue:", dominant_value) 
print("Eigenvector-based importance:") 
for node, score in zip(nodes, centrality): 
    print(f"{node}: {score:.4f}") 
# Verify Av = lambda*v 
v = np.real(eigenvectors[:, index]) 
print("Verification error:", 
np.linalg.norm(A @ v - dominant_value * v))
