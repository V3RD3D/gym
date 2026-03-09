# Evaluate Polynomial

## Background
Horner's method is an efficient algorithm for evaluating polynomials. It reduces the number of multiplications needed, transforming a polynomial of degree $n$ into a nested form.

## Task
Write a function `poly_evaluate(poly, x)` that evaluates a polynomial at a given value $x$. The polynomial is represented by a list of its coefficients, from the highest degree term to the constant term.

## Specifications
- The function takes a list of coefficients `poly` and a value `x`.
- It should return the evaluated polynomial as a number.
- Must implement Horner's method efficiently.

## Constraints
- The list `poly` will have at least one element.
- All elements in `poly` and `x` will be numbers.

## Example
```python
>>> poly_evaluate([2, -6, 2, -1], 3)
5
```

## Instructions
1. Implement the logic in `solution.py`.
2. Do not use `input()` or `print()`.
3. Test your solution locally before submitting.

[Solve Online](https://github.dev/matcom/gym/blob/main/exercises/poly_evaluate/solution.py) | [Ver en Español](./README.es.md), | [Leer en Español](README.es.md)
