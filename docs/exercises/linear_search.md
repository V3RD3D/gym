# Exercise: Linear Search

*[Leer en Español](README.es.md) | [Solve Online](https://github.dev/matcom/gym/blob/main/exercises/linear_search/solution.py)*

## Background/Motivation

Linear search is the simplest search algorithm. It works by iterating through a list element by element and comparing each one to a target value until a match is found or the end of the list is reached. It's an $O(n)$ operation because, in the worst case, you have to look at every single element once.

## The Task

Write a function `linear_search(items: list[int], target: int) -> int` that finds the **first index** of a target value in a list of integers.

### Specifications

- If the `target` is present in the `items` list, return its first index (0-based).
- If the `target` is not found, return `-1`.
- If the list is empty, return `-1`.

### Constraints

- `0 <= len(items) <= 10,000`
- `-10^9 <= target, items[i] <= 10^9`

### Example

```python
>>> linear_search([10, 20, 30, 40, 50], 30)
2
>>> linear_search([1, 2, 3, 4, 5], 10)
-1
>>> linear_search([], 5)
-1
```

## Instructions

1. Open `exercises/linear_search/solution.py`.
2. Implement the function.
3. Change `SUBMIT = False` to `SUBMIT = True` when ready.
4. Run `python solution.py` to verify with built-in self-tests.
