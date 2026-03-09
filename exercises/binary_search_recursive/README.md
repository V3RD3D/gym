# Recursive Binary Search

## Background
Binary search is a fast search algorithm with a time complexity of $O(\log n)$. It works on sorted arrays by repeatedly dividing the search interval in half. Implementing it recursively is a classic divide-and-conquer pattern where we adjust the bounds of our search in each recursive call.

## Task
Implement a recursive binary search that finds the index of a `target` element in a sorted list `lst`.

## Specifications
- **Input:** A sorted list of integers `lst` and an integer `target`.
- **Output:** The index of `target` in the list, or `-1` if the target is not found.

## Constraints
- The list will be sorted in ascending order.
- You must use a recursive approach. Do not use iterative loops or the `.index()` method.
- You should implement the function using the optional `low` and `high` parameters to track the current search interval.

## Example
```python
>>> binary_search_recursive([1, 2, 3, 4, 5], 4)
3
>>> binary_search_recursive([1, 2, 3, 4, 5], 6)
-1
```

## Instructions
1. Implement the `binary_search_recursive` function.
2. Initialize `high` properly if it's not provided.
3. Determine the middle index, check if it matches the target, and make the correct recursive call based on the value.
4. Return `-1` when the target cannot be found.

[Solve Online](https://github.dev/matcom/gym/blob/main/exercises/binary_search_recursive/solution.py), | [Leer en Español](README.es.md)
