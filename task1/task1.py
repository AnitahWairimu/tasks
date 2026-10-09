import numpy as np
import argparse


def calculate(operation: str, values: np.ndarray) -> float | np.ndarray:
	if operation == "add":
		return np.add.reduce(values)
	if operation == "subtract":
		return np.subtract.reduce(values)
	if operation == "multiply":
		return np.multiply.reduce(values)
	if operation == "divide":
		if np.any(values[1:] == 0):
			raise ValueError("cannot divide by zero")
		return np.divide.reduce(values)
	if operation == "mean":
		return np.mean(values)
	if operation == "sum":
		return np.sum(values)
	if operation == "min":
		return np.min(values)
	if operation == "max":
		return np.max(values)
	if operation == "square":
		return np.square(values)
	raise ValueError(f"unsupported operation: {operation}")


def main() -> None:
	parser = argparse.ArgumentParser(description="A calculator powered by NumPy.")
	parser.add_argument(
		"operation",
		choices=["add", "subtract", "multiply", "divide", "mean", "sum", "min", "max", "square"],
		help="the calculation to perform",
	)
	parser.add_argument("values", nargs="+", type=float, help="numbers to calculate with")
	args = parser.parse_args()

	values = np.array(args.values)
	try:
		result = calculate(args.operation, values)
	except ValueError as error:
		parser.error(str(error))
	print(result)


if __name__ == "__main__":
	main()
