# Búsqueda Binaria Recursiva

## Conocimientos Previos
La búsqueda binaria es un algoritmo rápido con una complejidad temporal de $O(\log n)$. Funciona en arreglos ordenados dividiendo repetidamente el intervalo de búsqueda a la mitad. Implementarlo de forma recursiva es un patrón clásico de "divide y vencerás" en el que ajustamos los límites de nuestra búsqueda en cada llamada recursiva.

## Tarea
Implementa una búsqueda binaria recursiva que encuentre el índice de un elemento `target` en una lista ordenada `lst`.

## Especificaciones
- **Entrada:** Una lista ordenada de números enteros `lst` y un número entero `target`.
- **Salida:** El índice de `target` en la lista, o `-1` si el objetivo no se encuentra.

## Restricciones
- La lista estará ordenada de forma ascendente.
- Debes usar un enfoque recursivo. No uses bucles iterativos o el método `.index()`.
- Debes implementar la función usando los parámetros opcionales `low` y `high` para mantener el intervalo de búsqueda actual.

## Ejemplo
```python
>>> binary_search_recursive([1, 2, 3, 4, 5], 4)
3
>>> binary_search_recursive([1, 2, 3, 4, 5], 6)
-1
```

## Instrucciones
1. Implementa la función `binary_search_recursive`.
2. Inicializa `high` correctamente si no se proporciona.
3. Determina el índice central, verifica si coincide con el objetivo, y haz la llamada recursiva correcta según el valor.
4. Devuelve `-1` cuando no se pueda encontrar el objetivo.

[Resuélvelo en línea](https://github.dev/matcom/gym/blob/main/exercises/binary_search_recursive/solution.py), | [Read in English](README.md)
