# Task 11: Newton-Raphson and Secant Methods

## Inputs and operation
The program solves `x^3 - 2x - 5 = 0`. Newton-Raphson uses a starting value, while the secant method uses two starting values and approximates the derivative numerically.

## Changed input
Changing the starting values changes the convergence path and may cause convergence to a different root or failure for a difficult function.

## Interpretation
The returned root is the point where the nonlinear equation is approximately zero. Comparing the methods illustrates the trade-off between derivative information and simplicity.

## Related Kenyan case
These methods can calibrate a groundwater-pump setting in a Kenyan borehole. Assumptions: a measured performance equation maps pump setting to target flow, and the desired setting is the equation's root.
