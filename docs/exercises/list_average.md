# Exercise: Computing Average

*[Leer en Español](README.es.md) | [Solve Online](https://github.dev/matcom/gym/blob/main/exercises/list_average/solution.py)*

## Background/Motivation

The arithmetic mean, often simply called the average, is one of the most common statistical measures. It provides a central value for a set of numbers and is used in everything from school grades to scientific research. In programming, calculating an average is a fundamental exercise to practice the accumulator pattern and handling collections of data.

## The Task

Implement a function `list_average(numbers: list[float]) -> float` that returns the arithmetic mean of a list of numbers.

### Specifications

- **Function Name**: `list_average`
- **Arguments**: `numbers` (list of float)
- **Return Type**: `float`
- **Expected Output**: The sum of all elements divided by the number of elements. If the list is empty, return `0.0`.

### Constraints

- $0 \le \text{len(numbers)} \le 10^5$
- The numbers can be integers or floats.

### Example

```python
>>> list_average([1, 2, 3, 4, 5])
3.0
>>> list_average([10, 20, 30])
20.0
```

## Instructions

1. Open `exercises/list_average/solution.py`.
2. Implement the `list_average` function.
3. Change `SUBMIT = False` to `SUBMIT = True` at the top of the file when you are ready to be graded.
4. Run `python solution.py` locally to verify your solution with the built-in self-tests.
