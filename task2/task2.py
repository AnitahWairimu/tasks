import numpy as np


def main() -> None:
    readings = np.array([20.0, 21.5, 22.0, 23.5, 24.0, 23.0])
    print("Readings:", readings)
    print(f"Mean: {np.mean(readings):.2f}")
    print(f"Minimum: {np.min(readings):.2f}")
    print(f"Maximum: {np.max(readings):.2f}")
    print("Fahrenheit:", np.round(1.8 * readings + 32, 2))


if __name__ == "__main__":
    main()
