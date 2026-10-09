import numpy as np
from scipy.integrate import solve_ivp


def cooling(_: float, temperature: np.ndarray) -> np.ndarray:
    return -0.2 * (temperature - 25.0)


def main() -> None:
    result = solve_ivp(cooling, (0.0, 10.0), [90.0], t_eval=[0.0, 5.0, 10.0])
    print("Times:", result.t)
    print("Temperatures:", np.round(result.y[0], 2))


if __name__ == "__main__":
    main()
