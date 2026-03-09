# Character Frequency

## Background
Calculating the frequency of characters in a text is a foundational step in cryptography, data compression (like Huffman coding), and natural language processing.

## Task
Write a function `char_frequency(s: str) -> dict[str, int]` that takes a string and returns a dictionary where keys are the characters from the string and values are their corresponding frequencies (counts).

## Specifications
- **Input**: A string `s` of arbitrary length.
- **Output**: A dictionary mapping each character to an integer representing how many times it appears in `s`.

## Constraints
- Do not use `input()` or `print()`.
- The case of characters matters (e.g., 'A' and 'a' are different).
- Whitespace and punctuation should be counted.
- If the string is empty, return an empty dictionary.

## Example
```python
>>> char_frequency("hello")
{'h': 1, 'e': 1, 'l': 2, 'o': 1}
>>> char_frequency("aA")
{'a': 1, 'A': 1}
```

## Instructions
Implement the function in `solution.py`. A dictionary is ideal for storing character counts.

[Solve Online](https://judge.matcom.uh.cu/arena/exercise/char_frequency) | [Leer en Español](README.es.md)
