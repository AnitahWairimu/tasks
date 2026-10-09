import numpy as np


def main() -> None:
    network = np.array([[0.0, 1.0, 1.0], [1.0, 0.0, 1.0], [1.0, 1.0, 0.0]])
    eigenvalues, eigenvectors = np.linalg.eig(network)
    index = np.argmax(eigenvalues.real)
    centrality = np.abs(eigenvectors[:, index].real)
    centrality /= np.sum(centrality)
    print("Eigenvalues:", eigenvalues)
    print("Normalized centrality:", centrality)


if __name__ == "__main__":
    main()
