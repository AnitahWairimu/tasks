import numpy as np


def main() -> None:
    time = np.linspace(0.0, 10.0, 101)
    temperature = np.empty_like(time)
    temperature[0] = 90.0
    ambient = 25.0
    rate = 0.2
    for index in range(len(time) - 1):
        step = time[index + 1] - time[index]
        temperature[index + 1] = temperature[index] + step * rate * (ambient - temperature[index])
    print(f"Temperature after {time[-1]:.0f} minutes: {temperature[-1]:.2f}")


if __name__ == "__main__":
    main()
