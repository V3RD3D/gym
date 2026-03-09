# Exercise: Recursive Min/Max

*[Leer en Español](README.es.md) | [Solve Online](https://github.dev/matcom/gym/blob/main/exercises/recursive_min_max/solution.py)*

## Background/Motivation

Finding the minimum and maximum elements in an array is a common problem that can be solved efficiently using a Divide and Conquer approach. This exercise introduces students to the core D&C strategy: divide the problem into smaller subproblems, solve them recursively, and combine the results. It highlights how recursion can lead to more elegant and sometimes more efficient solutions than iterative methods for problems with self-similar substructures.

## The Task

Implement a function `recursive_min_max(arr: list[int]) -> tuple[int, int]` that finds both the minimum and maximum elements in a list of integers using recursion.

### Specifications

-   **Function Name**: `recursive_min_max`
-   **Arguments**: `arr` (list of integers)
-   **Return Type**: `tuple[int, int]`
-   **Expected Output**: A tuple containing the minimum and maximum values in the list. For an empty list, behavior is undefined (assume non-empty list for simplicity, or handle as specified).

### Constraints

-   The list can contain integers.
-   $1 \le 	ext{len(arr)} \le 10^5$

### Example

```python
>>> recursive_min_max([3, 1, 4, 1, 5, 9, 2, 6])
(1, 9)
>>> recursive_min_max([7])
(7, 7)
```

## Instructions

1.  Open `exercises/recursive_min_max/solution.py`.
2.  Implement the `recursive_min_max` function.
3.  Change `SUBMIT = False` to `SUBMIT = True` at the top of the file when you are ready to be graded.
4.  Run `python solution.py` locally to verify your solution with the built-in self-tests.
