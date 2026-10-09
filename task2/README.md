# Task 2: NumPy Arrays and Sensor Computation

## Inputs and operation
The program stores six sensor temperature readings in a NumPy array. It computes the mean, minimum, maximum, and converts Celsius to Fahrenheit using `F = 1.8C + 32`.

## Changed input
Replacing one reading changes the statistics. Increasing the highest reading raises the maximum and usually raises the mean, while the minimum may remain unchanged.

## Interpretation
The mean represents typical sensor conditions; minimum and maximum show the observed range. The Fahrenheit array expresses the same measurements in another unit.

## Related Kenyan case
The same method can summarize temperature readings from a weather station in Turkana County. Assumptions: readings are hourly, in Celsius, and represent one day. The output supports heat monitoring and agricultural planning.
