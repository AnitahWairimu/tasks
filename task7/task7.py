import numpy as np
from scipy.linalg import lu_factor, lu_solve


def main() -> None:
    matrix = np.array([[4.0, 2.0, 1.0], [2.0, 5.0, 2.0], [1.0, 2.0, 4.0]])
    right_side = np.array([7.0, 4.0, 5.0])
    factorization = lu_factor(matrix)
    solution = lu_solve(factorization, right_side)
    print("LU solution:", solution)
    print("Residual:", matrix @ solution - right_side)


if __name__ == "__main__":
    main()
