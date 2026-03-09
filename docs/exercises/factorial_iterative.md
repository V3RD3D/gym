# Exercise: Iterative Factorial

*[Leer en Español](README.es.md) | [Solve Online](https://github.dev/matcom/gym/blob/main/exercises/factorial_iterative/solution.py)*

## Background/Motivation

The factorial of a non-negative integer $n$, denoted by $n!$, is the product of all positive integers less than or equal to $n$. Factorials are used in many areas of mathematics, including combinatorics, algebra, and mathematical analysis. Calculating a factorial is a classic example used to teach loop-based accumulation and is often compared with its recursive implementation.

## The Task

Implement a function `factorial_iterative(n: int) -> int` that calculates the factorial of $n$ using a loop.

### Specifications

- **Function Name**: `factorial_iterative`
- **Arguments**: `n` (int)
- **Return Type**: `int`
- **Expected Output**: The value of $n!$. For $n=0$, $0! = 1$.

### Constraints

- $0 \le n \le 50$

### Example

```python
>>> factorial_iterative(0)
1
>>> factorial_iterative(5)
120
>>> factorial_iterative(10)
3628800
```

## Instructions

1. Open `exercises/factorial_iterative/solution.py`.
2. Implement the `factorial_iterative` function.
3. Change `SUBMIT = False` to `SUBMIT = True` at the top of the file when you are ready to be graded.
4. Run `python solution.py` locally to verify your solution with the built-in self-tests.
