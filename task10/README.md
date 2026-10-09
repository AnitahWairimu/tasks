# Task 10: Bisection and Fixed-Point Methods

## Inputs and operation
The program solves `x^2 - 2 = 0`. SciPy's bisection method searches within the bracket `[0, 2]`, while fixed-point iteration repeatedly applies `x = 0.5(x + 2/x)`.

## Changed input
Changing the bracket or starting value changes the iteration path. The bracket must still contain a sign change for bisection to guarantee a root.

## Interpretation
Both methods converge to the positive square root of 2. Bisection emphasizes reliability, while fixed-point iteration can converge faster when the iteration function is suitable.

## Related Kenyan case
The method can estimate a break-even ticket price for a Kenyan transport route. Assumptions: a function gives profit as a function of price and a root represents zero profit. The result identifies the break-even operating point.
