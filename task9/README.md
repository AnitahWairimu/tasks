# Task 9: Eigenvalues and Eigenvectors

## Inputs and operation
The input matrix represents connections between three network nodes. NumPy computes eigenvalues and eigenvectors; the eigenvector associated with the largest eigenvalue is normalized as a centrality score.

## Changed input
Adding or removing a connection changes the dominant eigenvector and therefore changes which nodes appear most important.

## Interpretation
A larger centrality value means a node is strongly connected to other important nodes. Eigenvalues also describe structural modes of the network.

## Related Kenyan case
The same technique can rank important intersections in Nairobi's road network. Assumptions: matrix entries represent connection strength and traffic influence follows network links. The ranking can guide traffic monitoring or infrastructure improvements.
