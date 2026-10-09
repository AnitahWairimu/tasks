# Task 12: Polynomial and Nonlinear Equation Solving

## Inputs and operation
The program solves two coupled nonlinear equations with SciPy's `root`: a circular constraint and a linear relationship between two unknowns.

## Changed input
Changing the initial guess can lead to a different valid solution when multiple solutions exist. Changing a constant changes the intersection being calculated.

## Interpretation
The output is the coordinate where both equations are satisfied. The residual vector should be close to zero.

## Related Kenyan case
This approach can locate the intersection of a road alignment and a circular safety boundary in a Kenyan construction survey. Assumptions: coordinates are in a local planar system and the equations describe the road and boundary.
