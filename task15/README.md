# Task 15: Numerical Differentiation

## Inputs and operation
The program uses sampled position values from `s(t) = t^2 + 2t` and NumPy's `gradient` to estimate velocity, the derivative of position with respect to time.

## Changed input
Changing the sampling interval affects derivative accuracy. Finer sampling generally gives a better approximation, while noisy positions make the derivative less stable.

## Interpretation
The output is estimated speed at each time. It shows how quickly position changes rather than position itself.

## Related Kenyan case
This can estimate vehicle speed from GPS position readings on a Kenyan highway. Assumptions: timestamps are ordered and positions have been converted to a consistent distance unit. The result can support speed monitoring and road-safety analysis.
