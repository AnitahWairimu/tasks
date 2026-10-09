import numpy as np


def main() -> None:
    time = np.linspace(0.0, 4.0, 9)
    position = time**2 + 2 * time
    velocity = np.gradient(position, time)
    print("Time:", time)
    print("Estimated velocity:", np.round(velocity, 2))
    print("Velocity at t=2:", velocity[4])


if __name__ == "__main__":
    main()
