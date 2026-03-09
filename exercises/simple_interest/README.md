# Exercise: Simple Interest Calculator

*[Leer en Español](README.es.md) | [Solve Online](https://github.dev/matcom/gym/blob/main/exercises/simple_interest/solution.py)*

## Background/Motivation

Simple interest is a quick and easy method of calculating the interest charge on a loan. Simple interest is determined by multiplying the daily interest rate by the principal by the number of days that elapse between payments. It is commonly used in short-term loans and simple financial applications.

## The Task

Implement a function `simple_interest(principal: float, rate: float, time: float) -> float` that calculates simple interest using the formula:
$$I = \frac{P \times R \times T}{100}$$
where:
- $P$ is the Principal amount.
- $R$ is the Annual interest rate (in percent).
- $T$ is the Time (in years).

### Specifications

- **Function Name**: `simple_interest`
- **Arguments**: `principal` (float), `rate` (float), `time` (float)
- **Return Type**: `float`
- **Expected Output**: The calculated simple interest.

### Constraints

- $0 \le \text{principal}, \text{rate}, \text{time} \le 10^9$

### Example

```python
>>> simple_interest(1000, 5, 2)
100.0
>>> simple_interest(500, 3.5, 1)
17.5
```

## Instructions

1. Open `exercises/simple_interest/solution.py`.
2. Implement the `simple_interest` function.
3. Change `SUBMIT = False` to `SUBMIT = True` at the top of the file when you are ready to be graded.
4. Run `python solution.py` locally to verify your solution with the built-in self-tests.
