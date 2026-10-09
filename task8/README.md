# Task 8: Iterative Methods for Linear Systems

## Inputs and operation
The program applies the Jacobi method to a diagonally dominant two-equation system. Each iteration updates every unknown using the previous estimate.

## Changed input
Increasing the number of iterations usually reduces the residual and improves the approximation. A poorly conditioned or non-dominant matrix may converge slowly or fail to converge.

## Interpretation
The approximation is an estimated solution; the residual norm measures how closely it satisfies the equations.

## Related Kenyan case
This method can estimate pressures in a large Kenyan water-distribution network. Assumptions: the network equations are sparse and sufficiently well-conditioned. Iteration is useful when directly factorizing a very large system is expensive.
