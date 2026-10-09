from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import simpson, solve_ivp
from scipy.interpolate import CubicSpline, interp1d
from scipy.optimize import curve_fit, minimize, root_scalar


OUTPUT_DIR = Path(__file__).parent


def save_figure(number: int, title: str) -> None:
    plt.title(title)
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / f"task{number}_graph.png", dpi=160)
    plt.close()


def task2() -> None:
    readings = np.array([20.0, 21.5, 22.0, 23.5, 24.0, 23.0])
    hours = np.arange(1, len(readings) + 1)
    plt.figure()
    plt.plot(hours, readings, "o-", label="Celsius")
    plt.plot(hours, 1.8 * readings + 32, "s--", label="Fahrenheit")
    plt.xlabel("Hour")
    plt.ylabel("Temperature")
    plt.legend()
    save_figure(2, "Task 2: Sensor Temperature Readings")


def task3() -> None:
    values = np.arange(1, 11, dtype=float)
    plt.figure()
    plt.plot(values, values**2, "o-")
    plt.xlabel("Input value")
    plt.ylabel("Squared value")
    save_figure(3, "Task 3: Vectorized Squaring")


def task4() -> None:
    counts = np.arange(1, 101)
    errors = np.abs(np.array([sum(0.1 for _ in range(count)) for count in counts]) - 0.1 * counts)
    plt.figure()
    plt.plot(counts, errors)
    plt.xlabel("Number of additions")
    plt.ylabel("Absolute floating-point error")
    save_figure(4, "Task 4: Accumulated Floating-Point Error")


def task5() -> None:
    points = np.array([[1.0, 0.0], [0.0, 1.0], [2.0, 3.0]])
    angle = np.deg2rad(45)
    rotation = np.array([[np.cos(angle), -np.sin(angle)], [np.sin(angle), np.cos(angle)]])
    transformed = points @ rotation.T
    plt.figure()
    plt.scatter(points[:, 0], points[:, 1], label="Original")
    plt.scatter(transformed[:, 0], transformed[:, 1], label="Rotated")
    for original, rotated in zip(points, transformed):
        plt.plot([original[0], rotated[0]], [original[1], rotated[1]], "k:")
    plt.axis("equal")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    save_figure(5, "Task 5: Matrix Rotation")


def task6() -> None:
    matrix = np.array([[3.0, 1.0], [1.0, 2.0]])
    right_side = np.array([9.0, 8.0])
    solution = np.linalg.solve(matrix, right_side)
    plt.figure()
    plt.bar(["x", "y"], solution)
    plt.ylabel("Solved quantity")
    save_figure(6, "Task 6: Linear-System Solution")


def task7() -> None:
    matrix = np.array([[4.0, 2.0, 1.0], [2.0, 5.0, 2.0], [1.0, 2.0, 4.0]])
    right_side = np.array([7.0, 4.0, 5.0])
    from scipy.linalg import lu_factor, lu_solve

    solution = lu_solve(lu_factor(matrix), right_side)
    residual = matrix @ solution - right_side
    plt.figure()
    plt.bar(["Eq. 1", "Eq. 2", "Eq. 3"], residual)
    plt.axhline(0, color="black", linewidth=0.8)
    plt.ylabel("Residual")
    save_figure(7, "Task 7: LU-Decomposition Residual")


def task8() -> None:
    matrix = np.array([[5.0, 1.0], [2.0, 6.0]])
    right_side = np.array([11.0, 14.0])
    estimate = np.zeros(2)
    diagonal = np.diag(matrix)
    remainder = matrix - np.diagflat(diagonal)
    residuals = []
    for _ in range(25):
        estimate = (right_side - remainder @ estimate) / diagonal
        residuals.append(np.linalg.norm(matrix @ estimate - right_side))
    plt.figure()
    plt.semilogy(range(1, 26), residuals, "o-")
    plt.xlabel("Iteration")
    plt.ylabel("Residual norm")
    save_figure(8, "Task 8: Jacobi Convergence")


def task9() -> None:
    network = np.array([[0.0, 1.0, 1.0], [1.0, 0.0, 1.0], [1.0, 1.0, 0.0]])
    eigenvalues, eigenvectors = np.linalg.eig(network)
    centrality = np.abs(eigenvectors[:, np.argmax(eigenvalues.real)].real)
    centrality /= centrality.sum()
    plt.figure()
    plt.bar(["Node 1", "Node 2", "Node 3"], centrality)
    plt.ylabel("Normalized centrality")
    save_figure(9, "Task 9: Network Eigenvector Centrality")


def task10() -> None:
    function = lambda x: x**2 - 2
    result = root_scalar(function, bracket=[0.0, 2.0], method="bisect")
    upper = 2.0
    lower = 0.0
    errors = []
    for _ in range(20):
        midpoint = (lower + upper) / 2
        errors.append(abs(midpoint - result.root))
        if function(lower) * function(midpoint) <= 0:
            upper = midpoint
        else:
            lower = midpoint
    plt.figure()
    plt.semilogy(range(1, 21), errors, "o-")
    plt.xlabel("Bisection iteration")
    plt.ylabel("Absolute error")
    save_figure(10, "Task 10: Bisection Convergence")


def task11() -> None:
    function = lambda x: x**3 - 2 * x - 5
    derivative = lambda x: 3 * x**2 - 2
    value = 2.0
    values = [value]
    for _ in range(8):
        value -= function(value) / derivative(value)
        values.append(value)
    plt.figure()
    plt.plot(range(len(values)), values, "o-")
    plt.xlabel("Newton iteration")
    plt.ylabel("Root estimate")
    save_figure(11, "Task 11: Newton-Raphson Iteration")


def task12() -> None:
    x = np.linspace(-3, 3, 200)
    y = np.linspace(-3, 3, 200)
    xx, yy = np.meshgrid(x, y)
    plt.figure()
    plt.contour(xx, yy, xx**2 + yy**2 - 5, levels=[0], colors="blue")
    plt.contour(xx, yy, xx - yy - 1, levels=[0], colors="red")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend(["x^2 + y^2 = 5", "x - y = 1"])
    save_figure(12, "Task 12: Nonlinear Equation Intersection")


def task13() -> None:
    times = np.array([0.0, 1.0, 2.0, 3.0])
    measurements = np.array([10.0, 14.0, 13.0, 18.0])
    query = np.linspace(0, 3, 200)
    plt.figure()
    plt.scatter(times, measurements, label="Measurements")
    plt.plot(query, interp1d(times, measurements)(query), label="Linear")
    plt.plot(query, CubicSpline(times, measurements)(query), label="Cubic spline")
    plt.xlabel("Time")
    plt.ylabel("Measurement")
    plt.legend()
    save_figure(13, "Task 13: Interpolation")


def task14() -> None:
    time = np.arange(6, dtype=float)
    measurements = np.array([2.0, 2.7, 3.6, 4.8, 6.5, 8.7])
    model = lambda values, initial, rate: initial * np.exp(rate * values)
    parameters, _ = curve_fit(model, time, measurements, p0=[2.0, 0.3])
    query = np.linspace(0, 5, 200)
    plt.figure()
    plt.scatter(time, measurements, label="Measurements")
    plt.plot(query, model(query, *parameters), label="Exponential fit")
    plt.xlabel("Time")
    plt.ylabel("Value")
    plt.legend()
    save_figure(14, "Task 14: Exponential Curve Fit")


def task15() -> None:
    time = np.linspace(0, 4, 9)
    position = time**2 + 2 * time
    velocity = np.gradient(position, time)
    plt.figure()
    plt.plot(time, position, "o-", label="Position")
    plt.plot(time, velocity, "s-", label="Estimated velocity")
    plt.xlabel("Time")
    plt.legend()
    save_figure(15, "Task 15: Position and Numerical Velocity")


def task16() -> None:
    time = np.linspace(0, 10, 101)
    speed = 3 + 0.5 * time
    distance = np.concatenate(([0], np.cumsum((speed[:-1] + speed[1:]) * np.diff(time) / 2)))
    plt.figure()
    plt.plot(time, distance, label=f"Distance = {simpson(speed, x=time):.2f}")
    plt.xlabel("Time")
    plt.ylabel("Cumulative distance")
    plt.legend()
    save_figure(16, "Task 16: Numerical Integration of Speed")


def task17() -> None:
    time = np.linspace(0, 10, 101)
    temperature = np.empty_like(time)
    temperature[0] = 90
    for index in range(len(time) - 1):
        temperature[index + 1] = temperature[index] + 0.1 * 0.2 * (25 - temperature[index])
    plt.figure()
    plt.plot(time, temperature)
    plt.xlabel("Time")
    plt.ylabel("Temperature")
    save_figure(17, "Task 17: Euler Cooling Model")


def task18() -> None:
    result = solve_ivp(lambda _, temperature: -0.2 * (temperature - 25), (0, 10), [90], t_eval=np.linspace(0, 10, 100))
    plt.figure()
    plt.plot(result.t, result.y[0])
    plt.xlabel("Time")
    plt.ylabel("Temperature")
    save_figure(18, "Task 18: Adaptive ODE Cooling Model")


def task19() -> None:
    cost = lambda values: (values[0] - 8) ** 2 + 2 * (values[1] - 3) ** 2
    result = minimize(cost, [0, 0], bounds=[(0, None), (0, None)])
    x = np.linspace(0, 12, 100)
    y = np.linspace(0, 6, 100)
    xx, yy = np.meshgrid(x, y)
    plt.figure()
    plt.contourf(xx, yy, (xx - 8) ** 2 + 2 * (yy - 3) ** 2, levels=20)
    plt.scatter(*result.x, color="red", label="Optimum")
    plt.xlabel("Production")
    plt.ylabel("Marketing")
    plt.legend()
    save_figure(19, "Task 19: Optimization Cost Surface")


def task20() -> None:
    generator = np.random.default_rng(42)
    samples = generator.uniform(0, 1, size=1_000_000)
    values = 4 * np.sqrt(1 - samples**2)
    cumulative = np.cumsum(values) / np.arange(1, len(values) + 1)
    plt.figure()
    plt.plot(np.arange(1, len(values) + 1, 10_000), cumulative[::10_000])
    plt.axhline(np.pi, color="red", linestyle="--", label="pi")
    plt.xlabel("Number of samples")
    plt.ylabel("Estimate")
    plt.legend()
    save_figure(20, "Task 20: Monte Carlo Estimate of Pi")


def main() -> None:
    for function in [task2, task3, task4, task5, task6, task7, task8, task9, task10,
                     task11, task12, task13, task14, task15, task16, task17, task18,
                     task19, task20]:
        function()
    print("Generated graphs for Tasks 2-20 in docs/")


if __name__ == "__main__":
    main()
