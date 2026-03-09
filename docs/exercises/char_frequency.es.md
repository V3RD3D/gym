# Frecuencia de Caracteres

## Contexto
Calcular la frecuencia de los caracteres en un texto es un paso fundamental en la criptografía, la compresión de datos (como la codificación de Huffman) y el procesamiento del lenguaje natural.

## Tarea
Escribe una función `char_frequency(s: str) -> dict[str, int]` que tome una cadena y devuelva un diccionario donde las claves sean los caracteres de la cadena y los valores sean sus correspondientes frecuencias (conteos).

## Especificaciones
- **Entrada**: Una cadena `s` de longitud arbitraria.
- **Salida**: Un diccionario que mapea cada carácter a un entero que representa cuántas veces aparece en `s`.

## Restricciones
- No uses `input()` ni `print()`.
- Distingue mayúsculas y minúsculas (por ejemplo, 'A' y 'a' son diferentes).
- Se deben contar los espacios en blanco y los signos de puntuación.
- Si la cadena está vacía, devuelve un diccionario vacío.

## Ejemplo
```python
>>> char_frequency("hello")
{'h': 1, 'e': 1, 'l': 2, 'o': 1}
>>> char_frequency("aA")
{'a': 1, 'A': 1}
```

## Instrucciones
Implementa la función en `solution.py`. Un diccionario es ideal para almacenar el conteo de caracteres.

[Resolver en Línea](https://judge.matcom.uh.cu/arena/exercise/char_frequency) | [Read in English](README.md)
