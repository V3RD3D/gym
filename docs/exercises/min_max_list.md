# Exercise: Min/Max of a List

*[Leer en Español](README.es.md) | [Solve Online](https://github.dev/matcom/gym/blob/main/exercises/min_max_list/solution.py)*

## Background/Motivation

Finding the minimum and maximum elements in a collection is a fundamental task. While Python provides built-in `min()` and `max()` functions, implementing this manually helps understand how to track state across multiple iterations. Efficiency is key: we want to find both values in a single pass through the list.

## The Task

Write a function `min_max_list(items: list[int]) -> tuple[int, int] | None` that returns a tuple containing the minimum and maximum values found in the list.

### Specifications

- Return a tuple `(min_value, max_value)`.
- You must iterate through the list **only once**.
- If the list is empty, return `None`.
- Do NOT use the built-in `min()` or `max()` functions.

### Constraints

- `0 <= len(items) <= 10,000`
- `-10^9 <= items[i] <= 10^9`

### Example

```python
>>> min_max_list([3, 1, 4, 1, 5, 9, 2, 6, 5])
(1, 9)
>>> min_max_list([10])
(10, 10)
>>> min_max_list([])
None
```

## Instructions

1. Open `exercises/min_max_list/solution.py`.
2. Implement the function.
3. Change `SUBMIT = False` to `SUBMIT = True` when ready.
4. Run `python solution.py` to verify with built-in self-tests.
