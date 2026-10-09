import numpy as np


def main() -> None:
    coefficients = np.array([[3.0, 1.0], [1.0, 2.0]])
    demand = np.array([9.0, 8.0])
    solution = np.linalg.solve(coefficients, demand)
    print("Unknown quantities:", solution)
    print("Residual:", coefficients @ solution - demand)


if __name__ == "__main__":
    main()
