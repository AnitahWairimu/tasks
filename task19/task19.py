import numpy as np
from scipy.optimize import minimize


def cost(values: np.ndarray) -> float:
    production, marketing = values
    return (production - 8.0) ** 2 + 2.0 * (marketing - 3.0) ** 2


def main() -> None:
    result = minimize(cost, x0=np.array([0.0, 0.0]), bounds=[(0.0, None), (0.0, None)])
    print("Optimal production and marketing:", np.round(result.x, 3))
    print(f"Minimum cost: {result.fun:.3f}")


if __name__ == "__main__":
    main()
