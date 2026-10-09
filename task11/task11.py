from scipy.optimize import newton


def equation(x: float) -> float:
    return x**3 - 2 * x - 5


def main() -> None:
    newton_root = newton(equation, x0=2.0)
    secant_root = newton(equation, x0=2.0, x1=3.0)
    print(f"Newton-Raphson root: {newton_root:.10f}")
    print(f"Secant root: {secant_root:.10f}")


if __name__ == "__main__":
    main()
