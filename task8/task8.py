import numpy as np


def jacobi(matrix: np.ndarray, right_side: np.ndarray, iterations: int = 25) -> np.ndarray:
    estimate = np.zeros_like(right_side, dtype=float)
    diagonal = np.diag(matrix)
    remainder = matrix - np.diagflat(diagonal)
    for _ in range(iterations):
        estimate = (right_side - remainder @ estimate) / diagonal
    return estimate


def main() -> None:
    matrix = np.array([[5.0, 1.0], [2.0, 6.0]])
    right_side = np.array([11.0, 14.0])
    solution = jacobi(matrix, right_side)
    print("Jacobi approximation:", solution)
    print("Residual norm:", np.linalg.norm(matrix @ solution - right_side))


if __name__ == "__main__":
    main()
