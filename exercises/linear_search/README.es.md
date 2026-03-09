# Ejercicio: Búsqueda Lineal

*[Read in English](README.md) | [Resolver en Línea](https://github.dev/matcom/gym/blob/main/exercises/linear_search/solution.py)*

## Antecedentes/Motivación

La búsqueda lineal es el algoritmo de búsqueda más simple. Funciona recorriendo una lista elemento por elemento y comparando cada uno con un valor objetivo hasta que se encuentra una coincidencia o se llega al final de la lista. Es una operación $O(n)$ porque, en el peor de los casos, hay que mirar cada elemento una vez.

## La Tarea

Escribe una función `linear_search(items: list[int], target: int) -> int` que encuentre el **primer índice** de un valor objetivo en una lista de enteros.

### Especificaciones

- Si el `target` está presente en la lista `items`, devuelve su primer índice (basado en 0).
- Si no se encuentra el `target`, devuelve `-1`.
- Si la lista está vacía, devuelve `-1`.

### Restricciones

- `0 <= len(items) <= 10,000`
- `-10^9 <= target, items[i] <= 10^9`

### Ejemplo

```python
>>> linear_search([10, 20, 30, 40, 50], 30)
2
>>> linear_search([1, 2, 3, 4, 5], 10)
-1
>>> linear_search([], 5)
-1
```

## Instrucciones

1. Abre `exercises/linear_search/solution.py`.
2. Implementa la función.
3. Cambia `SUBMIT = False` a `SUBMIT = True` cuando estés listo.
4. Ejecuta `python solution.py` para verificar con las autopruebas integradas.
