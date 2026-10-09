# Task 18: Numerical ODE Solution with SciPy

## Inputs and operation
The program solves the same cooling equation as Task 17 using SciPy's adaptive `solve_ivp` method and evaluates the solution at selected times.

## Changed input
Changing the initial temperature or ambient temperature changes the entire solution curve. Solver tolerances can also affect numerical accuracy.

## Interpretation
The temperature decreases toward ambient conditions. Compared with basic Euler integration, adaptive ODE solving automatically manages the step size for accuracy.

## Related Kenyan case
This can simulate temperature conditions in a Kenya Medical Supplies Authority cold-chain container. Assumptions: the container follows Newton-style cooling and external temperature is approximately constant over the short simulation.
