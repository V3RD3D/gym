# Conteo de Palabras

## Contexto
Contar el número de palabras en un documento es una tarea común en el procesamiento y análisis de texto. Una palabra se define típicamente como una secuencia de caracteres separada por espacios en blanco.

## Tarea
Escribe una función `word_count(s: str) -> int` que tome una cadena y devuelva el número de palabras que contiene.

## Especificaciones
- **Entrada**: Una cadena `s` de longitud arbitraria.
- **Salida**: Un entero que representa el conteo total de palabras.

## Restricciones
- No uses `input()` ni `print()`.
- Las palabras están separadas por cualquier cantidad de espacio en blanco (espacios, tabulaciones, saltos de línea).
- Una cadena vacía o una cadena con solo espacios en blanco debe devolver `0`.

## Ejemplo
```python
>>> word_count("Hello World")
2
>>> word_count("  Python   is  awesome!  ")
3
```

## Instrucciones
Implementa la función en `solution.py`.

[Resolver en Línea](https://judge.matcom.uh.cu/arena/exercise/word_count) | [Read in English](README.md)
