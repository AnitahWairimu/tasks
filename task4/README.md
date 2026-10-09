# Task 4: Floating-Point Arithmetic and Numerical Error

## Inputs and operation
The program adds `0.1` ten times and compares it with direct multiplication by ten. It calculates the absolute difference and checks the values with `np.isclose`.

## Changed input
Changing the repeated value or number of additions changes the accumulated rounding error. More operations can make the difference more visible.

## Interpretation
The small difference is caused by binary floating-point representation. `np.isclose` is more appropriate than exact equality when comparing computed decimal quantities.

## Related Kenyan case
The method applies to cumulative banking or M-Pesa interest calculations. Assumptions: transactions are stored as floating-point values and many small amounts are accumulated. A tolerance-based comparison helps detect genuine errors without rejecting harmless rounding differences.
