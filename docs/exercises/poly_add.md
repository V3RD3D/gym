# Polynomial Addition

## Background
Polynomial addition involves adding the coefficients of matching degree terms. If the polynomials have different degrees, the missing higher-degree terms can be treated as having a coefficient of 0.

## Task
Write a function `poly_add(poly1, poly2)` that returns the sum of two polynomials. Both polynomials are given as lists of coefficients from highest to lowest degree.

## Specifications
- The function takes two lists of coefficients `poly1` and `poly2`.
- It should return a new list representing the sum of the polynomials.
- The resulting list should not have leading zeros unless the polynomial is exactly 0.

## Constraints
- `poly1` and `poly2` will not be empty.
- The output should be normalized to not have unnecessary leading zeros.

## Example
```python
>>> poly_add([3, 0, 4], [1, 5])
[3, 1, 9]
```

## Instructions
1. Implement the logic in `solution.py`.
2. Do not use `input()` or `print()`.
3. Test your solution locally before submitting.

[Solve Online](https://github.dev/matcom/gym/blob/main/exercises/poly_add/solution.py) | [Ver en Español](./README.es.md), | [Leer en Español](README.es.md)
