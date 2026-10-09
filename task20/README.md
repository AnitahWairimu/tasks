# Task 20: Random Numbers and Monte Carlo Methods

## Inputs and operation
The program generates one million uniform random samples with a fixed seed and estimates pi by numerically integrating the upper quarter-circle. It also calculates the standard error.

## Changed input
Changing the sample count changes the estimate and usually reduces standard error as the sample count increases. Changing the random seed produces a different estimate.

## Interpretation
The estimate approaches pi as the number of random samples grows. Standard error describes the expected sampling variation in the estimate.

## Related Kenyan case
The same method can estimate drought risk for a Kenyan agricultural region when rainfall, crop yield, and water demand are uncertain. Assumptions: probability distributions are chosen from historical data and each simulation represents one possible season.
