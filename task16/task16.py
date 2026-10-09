import numpy as np
from scipy.integrate import simpson


def main() -> None:
    time = np.linspace(0.0, 10.0, 101)
    speed = 3.0 + 0.5 * time
    distance = simpson(speed, x=time)
    print(f"Distance travelled: {distance:.2f} units")


if __name__ == "__main__":
    main()
