import timeit
import numpy as np


def loop_square(values: list[float]) -> list[float]:
    return [value**2 for value in values]


def main() -> None:
    values = np.arange(1, 1_000_001, dtype=float)
    vectorized = np.square(values)
    loop_time = timeit.timeit(lambda: loop_square(values.tolist()), number=1)
    numpy_time = timeit.timeit(lambda: np.square(values), number=1)
    print(f"First and last squared values: {vectorized[0]}, {vectorized[-1]}")
    print(f"Loop time: {loop_time:.4f}s")
    print(f"NumPy time: {numpy_time:.4f}s")


if __name__ == "__main__":
    main()
