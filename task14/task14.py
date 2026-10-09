import numpy as np
from scipy.optimize import curve_fit


def model(time: np.ndarray, initial: float, rate: float) -> np.ndarray:
    return initial * np.exp(rate * time)


def main() -> None:
    time = np.arange(6, dtype=float)
    measurements = np.array([2.0, 2.7, 3.6, 4.8, 6.5, 8.7])
    parameters, _ = curve_fit(model, time, measurements, p0=[2.0, 0.3])
    fitted = model(time, *parameters)
    print(f"Initial value: {parameters[0]:.3f}")
    print(f"Growth rate: {parameters[1]:.3f}")
    print(f"RMSE: {np.sqrt(np.mean((fitted - measurements) ** 2)):.3f}")


if __name__ == "__main__":
    main()
