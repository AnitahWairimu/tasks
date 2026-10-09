# Task 13: Interpolation

## Inputs and operation
The program receives measurements at four known times and estimates the value at an unmeasured time using linear interpolation and a cubic spline.

## Changed input
Changing the query time changes both estimates. Adding more measured points can improve accuracy but may also create spline oscillations.

## Interpretation
The estimates provide a plausible missing measurement between known observations. Differences between linear and cubic results show the effect of the interpolation model.

## Related Kenyan case
This can estimate missing rainfall measurements from a Kenyan weather station. Assumptions: the missing time lies between valid observations and rainfall changes smoothly enough for interpolation.
