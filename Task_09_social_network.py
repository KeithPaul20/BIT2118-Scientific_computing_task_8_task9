import numpy as np

# Real-world case: Social network influence model
# Nodes represent students, edges represent friendships.
# Eigenvector centrality measures influence in the network.

# Adjacency matrix for a small social network
# Students: A, B, C, D, E
A = np.array([
    [0, 1, 1, 0, 0],  # A connected to B, C
    [1, 0, 1, 1, 0],  # B connected to A, C, D
    [1, 1, 0, 1, 1],  # C connected to A, B, D, E
    [0, 1, 1, 0, 1],  # D connected to B, C, E
    [0, 0, 1, 1, 0]   # E connected to C, D
])

# Compute eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)

# Find dominant eigenvalue
index = np.argmax(np.real(eigenvalues))
dominant_value = np.real(eigenvalues[index])

# Dominant eigenvector (influence scores)
dominant_vector = np.abs(np.real(eigenvectors[:, index]))

# Normalize to get influence percentages
centrality = dominant_vector / dominant_vector.sum()

students = ["A", "B", "C", "D", "E"]

print("Eigenvector Centrality (Influence Scores):")
for student, score in zip(students, centrality):
    print(f"{student}: {score:.4f}")

# Verification of eigenpair
v = np.real(eigenvectors[:, index])
error = np.linalg.norm(A @ v - dominant_value * v)
print("\nVerification error:", error)
