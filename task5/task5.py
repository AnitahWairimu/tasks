import numpy as np


def rotation_matrix(angle_degrees: float) -> np.ndarray:
    angle = np.deg2rad(angle_degrees)
    return np.array(
        [[np.cos(angle), -np.sin(angle)], [np.sin(angle), np.cos(angle)]]
    )


def transform_points(points: np.ndarray, angle_degrees: float) -> np.ndarray:
    return points @ rotation_matrix(angle_degrees).T


def polygon_area(points: np.ndarray) -> float:
    x_coordinates = points[:, 0]
    y_coordinates = points[:, 1]
    return float(
        0.5
        * abs(
            np.dot(x_coordinates, np.roll(y_coordinates, -1))
            - np.dot(y_coordinates, np.roll(x_coordinates, -1))
        )
    )


def main() -> None:
    points = np.array([[1.0, 0.0], [0.0, 1.0], [2.0, 3.0]])
    original_angle = 90.0
    changed_angle = 45.0

    original_transformed = transform_points(points, original_angle)
    changed_transformed = transform_points(points, changed_angle)
    print("Computer-graphics case")
    print("Input points:\n", points)
    print(f"Rotation by {original_angle:.0f} degrees:\n", np.round(original_transformed, 3))
    print(f"Changed rotation by {changed_angle:.0f} degrees:\n", np.round(changed_transformed, 3))
    print("Rotation determinant:", np.linalg.det(rotation_matrix(original_angle)))

    panel_corners = np.array([[-1.0, -0.5], [1.0, -0.5], [1.0, 0.5], [-1.0, 0.5]])
    panel_angle = 30.0
    rotated_panel = transform_points(panel_corners, panel_angle)
    print("\nKenyan solar-panel case")
    print("Assumption: a 2D local panel footprint is rotated to model its orientation.")
    print(f"Panel orientation: {panel_angle:.0f} degrees")
    print("Rotated panel corners:\n", np.round(rotated_panel, 3))
    print("Panel area before and after:", polygon_area(panel_corners), polygon_area(rotated_panel))


if __name__ == "__main__":
    main()
