import numpy as np
from scipy.interpolate import CubicSpline, interp1d


def main() -> None:
    times = np.array([0.0, 1.0, 2.0, 3.0])
    measurements = np.array([10.0, 14.0, 13.0, 18.0])
    query = 1.5
    linear_value = interp1d(times, measurements)(query)
    cubic_value = CubicSpline(times, measurements)(query)
    print(f"Linear estimate at {query}: {float(linear_value):.2f}")
    print(f"Cubic estimate at {query}: {float(cubic_value):.2f}")


if __name__ == "__main__":
    main()
