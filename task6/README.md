# Task 6: Solution of Linear Systems

## Inputs and operation
The coefficient matrix represents two simultaneous resource equations, and the right-hand-side vector contains their totals. `np.linalg.solve` calculates the unknown quantities without explicitly forming a matrix inverse.

## Changed input
Changing a demand value changes the corresponding solution and may affect both unknowns because the equations are coupled.

## Interpretation
The solution gives the quantities satisfying both equations. The residual confirms the difference between the calculated left-hand side and the required totals.

## Related Kenyan case
This can estimate allocation of water between two Nairobi supply zones. Assumptions: the coefficients represent distribution relationships and the right-hand side represents measured demand. The result gives the allocation required to meet demand.
