# Task 19: Numerical Optimization

## Inputs and operation
The program minimizes a cost function for two non-negative decisions: production and marketing. SciPy's `minimize` searches for the values with the lowest cost.

## Changed input
Changing the target values or cost weights changes the optimal decision. Bounds prevent negative allocations.

## Interpretation
The result is the least-cost combination under the stated model. The objective value is the minimum estimated cost, not a physical measurement by itself.

## Related Kenyan case
This can allocate a county's budget between water-pump production and public-awareness campaigns. Assumptions: both decisions have measurable quadratic costs and all other constraints are represented by the bounds or objective function.
