# BIT 2118 Scientific Computing
## Documentation of the 20 Coursework Items

**Project location:** `tasks/`  
**Language:** Python 3  
**Libraries:** NumPy, SciPy, Matplotlib  
**Purpose:** This document explains the mathematical idea, implementation, input changes, interpretation, and practical application of each coursework item.

> **Scope note:** The supplied coursework labels the prerequisite as the first item and provides task files for Tasks 2–20. The prerequisite is documented below so that the complete 20-item course sequence is represented.

<!-- Page 1 -->

# Page 1 — Setup and prerequisite

## 1. Prerequisite: Data Science Essentials with Python

Before attempting the scientific-computing exercises, a learner should be comfortable with Python variables, functions, loops, conditional statements, lists, NumPy arrays, plotting, and importing third-party packages. These skills are used repeatedly throughout the project.

Create or activate the project environment and install the requirements:

```bash
cd tasks
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

The requirements are:

- **NumPy** for arrays, vectorized arithmetic, linear algebra, random sampling, and norms.
- **SciPy** for factorization, root finding, interpolation, curve fitting, integration, ODE solving, and optimization.
- **Matplotlib** for visualizing numerical results.

Run an individual task from the project root, for example:

```bash
python tasks/task10/task10.py
```

The task programs print numerical results, while the corresponding figures are stored in `tasks/docs/`. Most programs follow the same workflow: define input data, apply a numerical operation, print or plot the result, change a parameter when required, and interpret the outcome.

## How to read the documentation

For every task, **inputs** identify the data and parameters, **operation** states the mathematical method, **changed input** describes a sensitivity check, and **interpretation** explains what the output means. The practical examples connect the numerical method to a possible Kenyan application; they are illustrative models and should not be treated as production systems without validation.

<!-- Page 2 -->

# Page 2 — Arrays, arithmetic, matrices, and linear systems

## 2. NumPy arrays and sensor computation

**Source:** `task2/task2.py` and `task2/README.md`  
Six Celsius readings are stored in a NumPy array. The program computes the mean, minimum, maximum, and Fahrenheit values using `F = 1.8C + 32`. Replacing a reading changes the summary statistics; increasing the maximum usually increases the mean while leaving the minimum unchanged. The results can summarize hourly weather-station readings in Turkana County for heat monitoring and agricultural planning.

## 3. Mathematical functions and vectorization

**Source:** `task3/task3.py` and `task3/README.md`  
One million values are squared using a Python loop and NumPy’s `np.square`. `timeit` compares execution time. Vectorized operations are generally faster because optimized numerical code processes whole arrays without Python-level iteration. Increasing the array size increases both workloads, making vectorization increasingly valuable for transaction, traffic, image, or simulation data.

## 4. Floating-point arithmetic and numerical error

**Source:** `task4/task4.py` and `task4/README.md`  
The program compares adding `0.1` repeatedly with multiplying `0.1` directly by the number of additions. Binary floating-point cannot represent every decimal exactly, so the two results may differ slightly. The difference is measured with an absolute error and checked with `np.isclose`. More additions or a different value can make accumulated rounding error more visible. Tolerance-based comparison is appropriate for cumulative financial or engineering calculations.

## 5. Matrix algebra and matrix operations

**Source:** `task5/task5.py` and `task5/README.md`  
Two-dimensional points are transformed with a rotation matrix:

```text
[ cos(theta)  -sin(theta) ]
[ sin(theta)   cos(theta) ]
```

The program first uses 90 degrees and then 45 degrees. Matrix multiplication changes direction while preserving length and area; the determinant is approximately one. The related solar-panel example rotates a rectangular panel footprint by 30 degrees, demonstrating how a local east–north coordinate model can support orientation studies.

## 6. Solution of linear systems

**Source:** `task6/task6.py` and `task6/README.md`  
`np.linalg.solve` finds the unknown vector in a two-equation system `Ax = b` without explicitly computing `A⁻¹`. Changing a demand value changes the coupled solution. The residual `Ax - b` checks accuracy. The method can represent allocation of water between two Nairobi supply zones when coefficients describe distribution relationships.

## 7. Gaussian elimination and LU decomposition

**Source:** `task7/task7.py` and `task7/README.md`  
SciPy’s `lu_factor` and `lu_solve` solve a three-equation system by separating the coefficient matrix into triangular factors. If only the right-hand side changes, the factorization can be reused for efficient repeated solutions. The residual confirms numerical accuracy. This is useful for repeated flow calculations in a fixed pipe network.

<!-- Page 3 -->

# Page 3 — Iteration and nonlinear equations

## 8. Iterative methods for linear systems

**Source:** `task8/task8.py` and `task8/README.md`  
The Jacobi method repeatedly updates each unknown using values from the previous iteration. The example is diagonally dominant, so the residual decreases steadily. Increasing the iteration count normally improves the estimate, but poorly conditioned or non-dominant systems may converge slowly or diverge. Iteration is useful for large sparse water-network systems where direct factorization is expensive.

## 9. Eigenvalues and eigenvectors

**Source:** `task9/task9.py` and `task9/README.md`  
The program computes eigenvalues and eigenvectors of a three-node connection matrix. The eigenvector belonging to the largest eigenvalue is normalized as an eigenvector-centrality score. A higher score indicates stronger connection to important nodes. Adding or removing a link changes the ranking. The same method can prioritize intersections in a Nairobi road network.

## 10. Bisection and fixed-point methods

**Source:** `task10/task10.py` and `task10/README.md`  
The equation `x² - 2 = 0` is solved with bisection on `[0, 2]` and fixed-point iteration `x_(n+1) = 0.5(x_n + 2/x_n)`. Bisection is reliable when the bracket contains a sign change; fixed-point iteration can be faster when its update function is suitable. The methods converge to the positive square root of two. A related use is finding a break-even ticket price for a transport route.

## 11. Newton–Raphson and secant methods

**Source:** `task11/task11.py` and `task11/README.md`  
For `x³ - 2x - 5 = 0`, Newton–Raphson uses a starting value and derivative information, while the secant method uses two starting values to approximate the derivative. The example converges rapidly to approximately `2.09455`. Starting values affect the path and can cause failure for difficult equations. The method can calibrate a borehole pump setting to achieve a target flow.

## 12. Polynomial and nonlinear equation solving

**Source:** `task12/task12.py` and `task12/README.md`  
SciPy’s `root` solves the coupled system `x² + y² - 5 = 0` and `x - y - 1 = 0`. The solution is an intersection of a circle and a line, and the residual vector should be close to zero. A different initial guess can select another valid intersection when multiple solutions exist. The approach can locate a road alignment crossing a circular safety boundary in a local survey coordinate system.

## 13. Interpolation

**Source:** `task13/task13.py` and `task13/README.md`  
Four measurements at known times are used to estimate an unmeasured value with linear interpolation and a cubic spline. Linear interpolation joins neighboring points directly; the spline produces a smooth curve. Changing the query time changes both estimates, while extra points can improve accuracy or introduce spline oscillation. The method can fill a missing rainfall measurement between valid weather-station observations.

<!-- Page 4 -->

# Page 4 — Approximation, rates, and accumulation

## 14. Curve fitting and approximation

**Source:** `task14/task14.py` and `task14/README.md`  
The program fits `y = initial · exp(rate · time)` to six growth measurements using `scipy.optimize.curve_fit`. The fitted initial value estimates the quantity at time zero, the rate describes exponential growth, and RMSE measures average error in the original units. Changing a measurement changes both parameters. The model can provide an initial approximation of solar-energy demand growth, provided the trend is genuinely exponential over the chosen period.

## 15. Numerical differentiation

**Source:** `task15/task15.py` and `task15/README.md`  
For position `s(t) = t² + 2t`, `np.gradient` estimates velocity from sampled position values. The derivative is the rate of position change, not the position itself; at `t = 2`, the exact velocity is 6 and the numerical estimate is close. Finer sampling generally improves the estimate, while noisy position data can make differentiation unstable. This supports vehicle-speed estimation from ordered GPS positions.

## 16. Numerical integration

**Source:** `task16/task16.py` and `task16/README.md`  
The speed function `v(t) = 3 + 0.5t` is integrated over `0 ≤ t ≤ 10` with Simpson’s rule. Integration converts speed into distance, producing approximately **55 distance units**. Changing the time interval or speed samples changes the total; additional samples usually improve the approximation for a smooth function. The same method can estimate distance, fuel use, energy, or total flow from sampled rate data.

## 17. Ordinary differential equations with Euler’s method

**Source:** `task17/task17.py` and `task17/README.md`  
The cooling equation `dT/dt = rate · (ambient - T)` is advanced one step at a time with Euler’s method. Starting at 90 and approaching ambient temperature 25 produces a decreasing curve. A smaller time step normally improves accuracy; a large step may be inaccurate or unstable. The model can approximate vaccine cooling during rural transport if the ambient temperature and cooling coefficient are reasonably constant.

## 18. Numerical ODE solution with SciPy

**Source:** `task18/task18.py` and `task18/README.md`  
The same cooling model is solved with SciPy’s adaptive `solve_ivp`. Unlike a fixed-step Euler implementation, the solver changes internal step sizes to meet its accuracy goals and returns values at requested times. Initial or ambient temperature changes affect the whole curve, and tolerances control the accuracy–cost trade-off. This is suitable for a more dependable cold-chain simulation, such as a medical-supply container.

<!-- Page 5 -->

# Page 5 — Optimization, simulation, and conclusions

## 19. Numerical optimization

**Source:** `task19/task19.py` and `task19/README.md`  
The program minimizes a quadratic cost for two non-negative decisions, production and marketing. `scipy.optimize.minimize` searches for the lowest objective value while bounds prevent negative allocations. Changing targets or cost weights changes the optimum. The contour graph shows the cost surface and the optimum near `(8, 3)`. A related application is allocating a county budget between water-pump production and public-awareness campaigns.

## 20. Random numbers and Monte Carlo methods

**Source:** `task20/task20.py` and `task20/README.md`  
One million seeded uniform samples are used to estimate π from the upper quarter-circle:

```text
π ≈ 4 · mean(sqrt(1 - x²))
```

The fixed seed makes the run reproducible, while the standard error measures sampling variation. More samples usually reduce standard error approximately in proportion to `1/sqrt(n)`, although a different seed gives a different estimate. The same uncertainty-sampling pattern can estimate drought risk when rainfall, crop yield, and water demand are modeled with distributions learned from historical data.

## Reproducibility and validation checklist

1. Use the project environment and install `tasks/requirements.txt`.
2. Run each task from the repository root and record its printed output.
3. Compare output with the graph in `tasks/docs/taskN_graph.png`.
4. Change one input or parameter at a time and explain the observed change.
5. Check residuals, errors, or standard errors where the task provides them.
6. Treat Kenyan case studies as simplified assumptions requiring real data and domain validation.

## Overall conclusion

The collection progresses from array computation and numerical accuracy to matrix methods, iterative solvers, nonlinear equations, interpolation, approximation, calculus, differential equations, optimization, and stochastic simulation. Together, the exercises show that scientific computing is not only about obtaining a number: a reliable solution also requires selecting an appropriate method, checking convergence or error, visualizing behavior, testing sensitivity to inputs, and interpreting the result in context.
