# Task 17: ODEs Using Euler's Method

## Inputs and operation
The program models cooling with `dT/dt = rate * (ambient - T)`. Euler's method advances the temperature one time step at a time.

## Changed input
Changing the time step changes the approximation. A larger step is faster but less accurate and can become unstable for some equations.

## Interpretation
The temperature moves toward the ambient value over time. The final output is the estimated temperature after ten minutes.

## Related Kenyan case
This can model cooling of vaccines during transport in rural Kenya. Assumptions: the surrounding temperature is constant and the cooling coefficient is known. The result helps assess whether storage conditions remain safe.
