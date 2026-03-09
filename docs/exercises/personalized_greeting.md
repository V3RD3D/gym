# Exercise: Personalized Greeting

*[Leer en Español](README.es.md) | [Solve Online](https://github.dev/matcom/gym/blob/main/exercises/personalized_greeting/solution.py)*

## Background/Motivation

Interacting with users often involves formatting strings to include personal information. Python's f-strings provide a powerful and readable way to perform string interpolation. In this exercise, you'll practice using f-strings with multiple variables.

## The Task

Write a function `personalized_greeting(name, age)` that takes a name (string) and an age (integer) and returns a greeting string in the format: `"Hello {name}, you are {age} years old"`.

### Specifications

- **Function Name**: `personalized_greeting`
- **Arguments**:
    - `name` (str): The person's name.
    - `age` (int): The person's age.
- **Return Value**:
    - `str`: The formatted greeting.

### Constraints

- `name` will be a non-empty string.
- `age` will be a positive integer.

### Example

```python
>>> personalized_greeting("Alice", 25)
'Hello Alice, you are 25 years old'
```

## Instructions

1. Open `exercises/personalized_greeting/solution.py`.
2. Implement the function.
3. Change `SUBMIT = False` to `SUBMIT = True` when ready.
4. Run `python solution.py` to verify with built-in self-tests.
