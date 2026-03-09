# Tail Recursive Fibonacci

## Background
The Fibonacci sequence is defined recursively as $F(n) = F(n-1) + F(n-2)$, with $F(0) = 0$ and $F(1) = 1$. The standard recursive solution branches exponentially ($O(2^n)$ time complexity), which is highly inefficient. Using tail recursion, we can pass the previous two values forward as state, optimizing the time complexity to $O(n)$.

## Task
Calculate the $n$-th Fibonacci number using a tail-recursive function.

## Specifications
- **Input:** An integer `n` ($n \ge 0$).
- **Output:** The $n$-th Fibonacci number.

## Constraints
- The function must be recursive.
- The recursive call must be the very last operation in the function.
- Do not use iterative loops.
- You must use accumulator arguments to track the state.

## Example
```python
>>> fibonacci_tail(5)
5
>>> fibonacci_tail(10)
55
```

## Instructions
1. Implement the `fibonacci_tail` function using tail recursion.
2. Initialize two accumulators (`a` and `b`) to track the previous two values in the sequence.
3. Validate your code with the provided tests.

[Solve Online](https://github.dev/matcom/gym/blob/main/exercises/fibonacci_tail/solution.py), | [Leer en Español](README.es.md)
