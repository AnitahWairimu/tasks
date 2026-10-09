import numpy as np


def main() -> None:
    generator = np.random.default_rng(42)
    samples = generator.uniform(0.0, 1.0, size=1_000_000)
    estimate = 4.0 * np.mean(np.sqrt(1.0 - samples**2))
    standard_error = 4.0 * np.std(np.sqrt(1.0 - samples**2), ddof=1) / np.sqrt(samples.size)
    print(f"Monte Carlo estimate of pi: {estimate:.6f}")
    print(f"Standard error: {standard_error:.6f}")


if __name__ == "__main__":
    main()
