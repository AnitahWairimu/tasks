from scipy.optimize import root_scalar


def equation(x: float) -> float:
    return x**2 - 2


def main() -> None:
    bisection = root_scalar(equation, bracket=[0.0, 2.0], method="bisect")
    fixed_point = 1.0
    for _ in range(20):
        fixed_point = 0.5 * (fixed_point + 2 / fixed_point)
    print(f"Bisection root: {bisection.root:.10f}")
    print(f"Fixed-point root: {fixed_point:.10f}")


if __name__ == "__main__":
    main()
