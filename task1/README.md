# Task 1: NumPy Calculator

## Inputs and operation
The user supplies an operation and one or more numeric values on the command line. NumPy stores the values in an array and performs arithmetic or statistical reductions such as addition, division, mean, minimum, maximum, and squaring.

## Changed input
Changing the numbers changes the returned result. For example, `mean 10 20 30` returns 20, while `mean 20 40 60` returns 40.

## Interpretation
The output is the calculated scalar or array result. Division by zero is rejected so that an invalid numerical result is not silently accepted.

## Related Kenyan case
The calculator can be used to summarize household electricity readings in Nairobi. Assumptions: readings are measured in kilowatt-hours and entered for several time periods. The mean gives average consumption, while `sum` gives total consumption for billing analysis.

Run it with:

```bash
.venv/bin/python task1.py mean 10 20 30
```
