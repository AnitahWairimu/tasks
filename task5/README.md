# Task 5: Matrix Algebra and Matrix Operations

## Inputs and mathematical operations

The computer-graphics case uses three 2D points:

```text
[[1, 0], [0, 1], [2, 3]]
```

Each point is multiplied by a rotation matrix:

```text
[[cos(theta), -sin(theta)],
 [sin(theta),  cos(theta)]]
```

The program first uses `theta = 90` degrees. It then changes the input to
`theta = 45` degrees. NumPy performs the matrix multiplication with `@` and
calculates the determinant with `np.linalg.det`.

## Output and interpretation

A positive rotation changes the direction of every point while preserving its
distance from the origin. The determinant is approximately `1`, which means
the transformation preserves orientation, lengths, and area. Changing the
angle from 90 to 45 degrees produces a smaller rotation, so the transformed
coordinates are different but the geometric shape is preserved.

## Related Kenyan case

The second example models a simplified solar-panel footprint for a solar farm
in Turkana County. The assumptions are:

- The panel is represented by a 2D rectangle of width 2 and height 1 units.
- The local ground coordinate system is flat and uses east and north axes.
- A 30-degree rotation represents a change in the panel's local orientation.
- This is a geometric orientation model, not a complete solar-radiation model.

The program rotates the four panel corners and reports the transformed
coordinates. The panel area remains unchanged because a rotation matrix has
determinant 1. In a more complete project, the orientation could be combined
with solar-position data and energy measurements to optimize panel placement.