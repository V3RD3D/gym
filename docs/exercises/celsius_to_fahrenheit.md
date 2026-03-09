# Exercise: Temperature Conversion

*[Leer en Español](README.es.md) | [Solve Online](https://github.dev/matcom/gym/blob/main/exercises/celsius_to_fahrenheit/solution.py)*

## Background/Motivation

Converting temperatures between different scales is a fundamental task in science and engineering. The Celsius scale, commonly used in most of the world, and the Fahrenheit scale, used primarily in the United States, are related by a linear equation. Implementing this conversion is a classic exercise to practice arithmetic precedence and floating-point operations.

## The Task

Implement a function `celsius_to_fahrenheit(celsius: float) -> float` that converts a temperature from Celsius to Fahrenheit using the formula:
$$F = (C \times \frac{9}{5}) + 32$$

### Specifications

- **Function Name**: `celsius_to_fahrenheit`
- **Arguments**: `celsius` (float)
- **Return Type**: `float`
- **Expected Output**: The temperature converted to Fahrenheit.

### Constraints

- $-273.15 \le \text{celsius} \le 10^6$ (Absolute zero to a very high value)

### Example

```python
>>> celsius_to_fahrenheit(0)
32.0
>>> celsius_to_fahrenheit(100)
212.0
>>> celsius_to_fahrenheit(-40)
-40.0
```

## Instructions

1. Open `exercises/celsius_to_fahrenheit/solution.py`.
2. Implement the `celsius_to_fahrenheit` function.
3. Change `SUBMIT = False` to `SUBMIT = True` at the top of the file when you are ready to be graded.
4. Run `python solution.py` locally to verify your solution with the built-in self-tests.
