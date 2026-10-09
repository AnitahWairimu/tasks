import numpy as np


def main() -> None:
    value = 0.1
    repeated_addition = sum(value for _ in range(10))
    direct_sum = value * 10
    print(f"Repeated addition: {repeated_addition:.17f}")
    print(f"Direct multiplication: {direct_sum:.17f}")
    print(f"Difference: {abs(repeated_addition - direct_sum):.3e}")
    print(f"Close according to NumPy: {np.isclose(repeated_addition, direct_sum)}")


if __name__ == "__main__":
    main()
