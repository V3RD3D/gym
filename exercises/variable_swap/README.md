# Exercise: Variable Swap

*[Leer en Español](README.es.md) | [Solve Online](https://github.dev/matcom/gym/blob/main/exercises/variable_swap/solution.py)*

## Background/Motivation

In many algorithms, it is necessary to exchange the values of two variables. In many programming languages, this requires a temporary third variable to hold one value while the other is being overwritten. However, Python provides an elegant and concise way to do this using tuple unpacking. This exercise explores both the logic of swapping and the Pythonic way to implement it.

## The Task

Implement a function `variable_swap(a: any, b: any) -> tuple[any, any]` that takes two values and returns them swapped in a tuple.

### Specifications

- **Function Name**: `variable_swap`
- **Arguments**: `a` (any), `b` (any)
- **Return Type**: `tuple[any, any]`
- **Expected Output**: A tuple `(b, a)`.

### Constraints

- The arguments can be of any data type.

### Example

```python
>>> variable_swap(5, 10)
(10, 5)
>>> variable_swap("apple", "banana")
('banana', 'apple')
```

## Instructions

1. Open `exercises/variable_swap/solution.py`.
2. Implement the `variable_swap` function.
3. Change `SUBMIT = False` to `SUBMIT = True` at the top of the file when you are ready to be graded.
4. Run `python solution.py` locally to verify your solution with the built-in self-tests.
