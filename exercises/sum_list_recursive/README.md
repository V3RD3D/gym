# Exercise: Recursive List Sum

*[Leer en Español](README.es.md) | [Solve Online](https://github.dev/matcom/gym/blob/main/exercises/sum_list_recursive/solution.py)*

## Background/Motivation

Recursion is a method of solving a computational problem where the solution depends on solutions to smaller instances of the same problem. For linear data structures like lists, the recursive step usually involves separating the first element (the head) from the rest of the list (the tail), and applying the function to the tail. This approach helps in understanding divide and conquer strategies and can lead to elegant solutions for certain problems.

## The Task

Implement a function `sum_list_recursive(lst: list[int]) -> int` that calculates the sum of all elements in a list using recursion.

### Specifications

- **Function Name**: `sum_list_recursive`
- **Arguments**: `lst` (list of integers)
- **Return Type**: `int`
- **Expected Output**: The sum of all elements in the list. For an empty list, the sum is 0.

### Constraints

- The list can contain integers.
- The length of the list can be up to $10^5$.

### Example

```python
>>> sum_list_recursive([1, 2, 3, 4])
10
>>> sum_list_recursive([])
0
```

## Instructions

1. Open `exercises/sum_list_recursive/solution.py`.
2. Implement the `sum_list_recursive` function.
3. Change `SUBMIT = False` to `SUBMIT = True` at the top of the file when you are ready to be graded.
4. Run `python solution.py` locally to verify your solution with the built-in self-tests.
