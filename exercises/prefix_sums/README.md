# Exercise: Cumulative Sums

*[Leer en Español](README.es.md) | [Solve Online](https://github.dev/matcom/gym/blob/main/exercises/prefix_sums/solution.py)*

## Background/Motivation

A cumulative sum (also known as a prefix sum) is a sequence of partial sums of a given sequence. For example, the cumulative sums of the sequence $\{a, b, c, \dots\}$ are $\{a, a+b, a+b+c, \dots\}$. This is a fundamental technique used in competitive programming and data analysis to quickly calculate the sum of any sub-range of a list in $O(1)$ time after a one-time $O(n)$ preprocessing step.

## The Task

Implement a function `prefix_sums(numbers: list[int]) -> list[int]` that takes a list of integers and returns a new list where each element at index $i$ is the sum of all elements from the original list from index $0$ to $i$.

### Specifications

- **Function Name**: `prefix_sums`
- **Arguments**: `numbers` (list of integers)
- **Return Type**: `list[int]`
- **Expected Output**: A list of the same length containing the cumulative sums.

### Constraints

- $0 \le \text{len(numbers)} \le 10^5$
- Elements are integers within the range $[-10^9, 10^9]$.

### Example

```python
>>> prefix_sums([1, 2, 3])
[1, 3, 6]
>>> prefix_sums([10, -10, 5])
[10, 0, 5]
```

## Instructions

1. Open `exercises/prefix_sums/solution.py`.
2. Implement the `prefix_sums` function.
3. Change `SUBMIT = False` to `SUBMIT = True` at the top of the file when you are ready to be graded.
4. Run `python solution.py` locally to verify your solution with the built-in self-tests.
