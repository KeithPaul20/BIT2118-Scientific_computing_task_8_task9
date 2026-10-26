# Task 9: Eigenvalues and Eigenvectors

## A. Input values and mathematical operation
- Input: Adjacency matrix **A** for a small undirected network with nodes A, B, C, D.
- Operation: Compute eigenvalues and eigenvectors using `np.linalg.eig(A)`, then select the dominant eigenvalue and its eigenvector.

## B. Parameter change
- Changing the adjacency matrix (e.g., adding or removing a connection between nodes) changes the eigenvalues and eigenvectors.
- This alters the centrality scores, meaning different nodes become more or less “important”.

## C. Meaning of the output
- The **dominant eigenvalue** indicates the strength of the most influential connectivity pattern in the network.
- The **dominant eigenvector**, after normalization, gives an importance score for each node (eigenvector-based centrality).
- Higher centrality value means the node is more structurally central in the network.

## D. Graph / interpretation (if you add a plot)
- A bar chart of centrality scores would show which node is most central.
- Nodes with more connections or better-positioned connections tend to have higher eigenvector centrality.

## E. Modified real-world case
- Case: Model a small social network (students in a class) where edges represent friendships.
- Input: Adjacency matrix of friendships.
- Output: Eigenvector centrality scores indicating which students are most “influential” in the network.
- Interpretation: Nodes with high centrality are key connectors or hubs in the social graph.
