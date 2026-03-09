# Exercise: Polynomial Multiplication

*[Leer en Español](README.es.md) | [Solve Online](https://github.dev/matcom/gym/blob/main/exercises/poly_mul/solution.py)*

## Background/Motivation

Polynomial multiplication is a fundamental operation in algebra with applications in various fields, including computer graphics, signal processing, and computer algebra systems. Understanding how to multiply polynomials efficiently is key to grasping more complex algorithms involving symbolic computation.

## The Task

Implement a function `poly_mul(poly1: list[int | float], poly2: list[int | float]) -> list[int | float]` that multiplies two polynomials. The polynomials are represented as lists of coefficients, where the index corresponds to the power of x. For example, `[c0, c1, c2]` represents $c_0 + c_1x + c_2x^2$.

### Specifications

-   **Function Name**: `poly_mul`
-   **Arguments**: `poly1` (list of coefficients), `poly2` (list of coefficients)
-   **Return Type**: `list[int | float]`
-   **Expected Output**: A list representing the coefficients of the resulting polynomial.

### Constraints

-   Polynomials will have at least one coefficient.
-   Coefficients will be integers or floats.

### Example

```python
>>> poly_mul([1, 2], [3, 4]) # (1 + 2x) * (3 + 4x) = 3 + 4x + 6x + 8x^2 = 3 + 10x + 8x^2
[3, 10, 8]
>>> poly_mul([1, 0, 1], [1, 1]) # (1 + x^2) * (1 + x) = 1 + x + x^2 + x^3
[1, 1, 1, 1]
```

## Instructions

1.  Open `exercises/poly_mul/solution.py`.
2.  Implement the `poly_mul` function.
3.  Change `SUBMIT = False` to `SUBMIT = True` at the top of the file when you are ready to be graded.
4.  Run `python solution.py` locally to verify your solution with the built-in self-tests.
