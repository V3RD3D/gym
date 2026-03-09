# Multiplicación de Matrices

## Contexto
La multiplicación de matrices implica calcular el producto escalar de las filas de la primera matriz y las columnas de la segunda. El número de columnas de la primera matriz debe coincidir con el número de filas de la segunda.

## Tarea
Escribe una función `matrix_mul(mat1, mat2)` que multiplique dos matrices.

## Especificaciones
- La función toma dos listas 2D `mat1` y `mat2`.
- Debe devolver su producto matricial como una nueva lista 2D.

## Restricciones
- Las matrices tendrán dimensiones compatibles: $M \times N$ y $N \times P$.
- Las matrices no estarán vacías.

## Ejemplo
```python
>>> matrix_mul([[1, 2], [3, 4]], [[2, 0], [1, 2]])
[[4, 4], [10, 8]]
```

## Instrucciones
1. Implementa la lógica en `solution.py`.
2. No uses `input()` ni `print()`.
3. Prueba tu solución localmente antes de enviarla.

[Resolver en Línea](https://github.dev/matcom/gym/blob/main/exercises/matrix_mul/solution.py) | [View in English](./README.md), | [Read in English](README.md)
