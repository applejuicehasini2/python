def newton_raphson_sqrt(number, iterations=5):
  """Calculates the square root of a number using Newton-Raphson's method.

  Args:
    number: The number for which to calculate the square root.
    iterations: The number of iterations to perform (default is 5).

  Returns:
    The approximate square root of the number.
  """
  if number < 0:
    return float('NaN')

  guess = number / 2.0
  for _ in range(iterations):
    guess = 0.5 * (guess + number / guess)
  return guess

# Example usage:
num = 25
result = newton_raphson_sqrt(num)
print(f"The square root of {num} (Newton-Raphson) is {result}")

num = -4
result = newton_raphson_sqrt(num)
print(f"The square root of {num} (Newton-Raphson) is {result}")