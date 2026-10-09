import numpy as np
from scipy.optimize import root


def equations(values: np.ndarray) -> np.ndarray:
    x, y = values
    return np.array([x**2 + y**2 - 5, x - y - 1])


def main() -> None:
    solution = root(equations, x0=np.array([2.0, 1.0]))
    print("Solution:", solution.x)
    print("Residual:", equations(solution.x))


if __name__ == "__main__":
    main()
