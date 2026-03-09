# Exercise: Case Inverter

*[Leer en Español](README.es.md) | [Solve Online](https://github.dev/matcom/gym/blob/main/exercises/case_inverter/solution.py)*

## Background/Motivation

Text data often comes in inconsistent cases. Being able to programmatically flip the case of characters (converting lowercase to uppercase and vice-versa) is a common string manipulation task with applications in data cleaning, text processing, and user input validation.

## The Task

Implement a function `case_inverter(s: str) -> str` that takes a string and returns a new string with the case of each character inverted.

### Specifications

-   **Function Name**: `case_inverter`
-   **Arguments**: `s` (str)
-   **Return Type**: `str`
-   **Expected Output**: A new string with the case of each character inverted.

### Constraints

-   The input string can contain letters, numbers, spaces, and symbols.

### Example

```python
>>> case_inverter("Hello World!")
"hELLO wORLD!"
>>> case_inverter("Python 3.12")
"pYTHON 3.12"
```

## Instructions

1.  Open `exercises/case_inverter/solution.py`.
2.  Implement the `case_inverter` function.
3.  Change `SUBMIT = False` to `SUBMIT = True` at the top of the file when you are ready to be graded.
4.  Run `python solution.py` locally to verify your solution with the built-in self-tests.
