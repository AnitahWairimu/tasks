# Task 7: Gaussian Elimination and LU Decomposition

## Inputs and operation
The program solves a three-equation linear system using SciPy's `lu_factor` and `lu_solve`. LU decomposition separates the matrix into triangular factors for efficient repeated solves.

## Changed input
Changing the right-hand-side vector represents a new demand scenario. The factorization can be reused while only the solution vector changes.

## Interpretation
The solution satisfies the three system equations, and the residual shows numerical accuracy.

## Related Kenyan case
The model can represent repeated water-flow calculations in Nairobi's pipe network. Assumptions: the coefficient matrix describes pipe connections and each demand scenario uses the same network. LU decomposition is useful when many demand cases must be tested.
