# Exercise: Most Common Element

*[Leer en Español](README.es.md) | [Solve Online](https://github.dev/matcom/gym/blob/main/exercises/list_mode/solution.py)*

## Background/Motivation

In statistics, the mode is the value that appears most often in a set of data. Finding the mode is a practical application of frequency counting, which is a common task in data analysis, natural language processing, and many other fields. In Python, this is typically solved using a dictionary to map each element to its occurrence count.

## The Task

Implement a function `list_mode(items: list[Any]) -> Any` that returns the most frequent element in a list. If the list is empty, return `None`. If there is a tie between multiple elements, you may return any one of them.

### Specifications

- **Function Name**: `list_mode`
- **Arguments**: `items` (list of any type)
- **Return Type**: `Any` (the most frequent element)
- **Expected Output**: The element with the highest frequency.

### Constraints

- $0 \le \text{len(items)} \le 10^5$
- Elements can be of any hashable type (integers, strings, etc.).

### Example

```python
>>> list_mode([1, 2, 2, 3, 3, 3])
3
>>> list_mode(['a', 'b', 'a'])
'a'
```

## Instructions

1. Open `exercises/list_mode/solution.py`.
2. Implement the `list_mode` function.
3. Change `SUBMIT = False` to `SUBMIT = True` at the top of the file when you are ready to be graded.
4. Run `python solution.py` locally to verify your solution with the built-in self-tests.
