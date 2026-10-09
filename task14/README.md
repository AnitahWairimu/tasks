# Task 14: Curve Fitting and Approximation

## Inputs and operation
The program fits an exponential model `y = initial * exp(rate * time)` to measured growth data using SciPy's `curve_fit`. It reports fitted parameters and root-mean-square error.

## Changed input
Changing a measurement changes the fitted initial value and growth rate. Noisy data generally increases the RMSE.

## Interpretation
The initial value estimates the quantity at time zero, while the rate describes exponential growth. RMSE summarizes the average fitting error in the original units.

## Related Kenyan case
The model can approximate growth in solar-energy demand in Kenya. Assumptions: demand follows an approximately exponential trend over the selected period and measurements are comparable.
