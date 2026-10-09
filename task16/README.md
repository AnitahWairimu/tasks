# Task 16: Numerical Integration

## Inputs and operation
The program integrates a speed function sampled over ten time units using SciPy's Simpson rule. Integration converts speed into travelled distance.

## Changed input
Changing the time interval or speed values changes the calculated distance. More samples can improve the approximation for a smooth speed curve.

## Interpretation
The result is the total distance travelled over the interval, measured in distance units.

## Related Kenyan case
The method can estimate fuel or energy consumption from sampled vehicle speed and power data on a Kenyan transport route. Assumptions: samples are time-ordered and the measured rate is integrated over time.
