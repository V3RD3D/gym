# Exercise: Primality Test

*[Leer en Español](README.es.md) | [Solve Online](https://github.dev/matcom/gym/blob/main/exercises/prime_check/solution.py)*

## Background/Motivation

A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. Determining whether a number is prime is a fundamental problem in number theory and has vast applications in cryptography, such as the RSA algorithm. While a naive approach of testing all numbers up to $n$ works, a more efficient method is to test only up to $\sqrt{n}$, as any factor larger than the square root must have a corresponding factor smaller than it.

## The Task

Implement a function `prime_check(n: int) -> bool` that returns `True` if $n$ is prime and `False` otherwise.

### Specifications

- **Function Name**: `prime_check`
- **Arguments**: `n` (int)
- **Return Type**: `bool`
- **Expected Output**: `True` if prime, `False` otherwise.

### Constraints

- $0 \le n \le 10^9$

### Example

```python
>>> prime_check(2)
True
>>> prime_check(4)
False
>>> prime_check(17)
True
```

## Instructions

1. Open `exercises/prime_check/solution.py`.
2. Implement the `prime_check` function.
3. Change `SUBMIT = False` to `SUBMIT = True` at the top of the file when you are ready to be graded.
4. Run `python solution.py` locally to verify your solution with the built-in self-tests.
