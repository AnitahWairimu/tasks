# Task 3: Vectorization

## Inputs and operation
The program squares one million values using both a Python list comprehension and NumPy's vectorized `np.square` operation. `timeit` compares their execution times.

## Changed input
Increasing the array size increases both execution times, but vectorization generally remains more efficient because NumPy performs the operation in optimized numerical code.

## Interpretation
The first and last values confirm that every element was squared. The timing comparison demonstrates why vectorization is important for large scientific datasets.

## Related Kenyan case
This can process large mobile-money transaction or network-traffic datasets in Kenya. Assumptions: each value is an independent numeric measurement and the same transformation is applied to all records. Vectorization reduces processing time for national-scale data.
