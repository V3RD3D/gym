# Ejercicio: Mínimo/Máximo Recursivo

*[Read in English](README.md) | [Solve Online](https://github.dev/matcom/gym/blob/main/exercises/recursive_min_max/solution.py)*

## Antecedentes/Motivación

Encontrar tanto el elemento mínimo como el máximo en un arreglo se puede hacer de manera eficiente utilizando un enfoque de Divide y Vencerás. Este ejercicio introduce a los estudiantes la estrategia central de D&C: dividir el problema en subproblemas más pequeños, resolverlos recursivamente y combinar los resultados. Destaca cómo la recursión puede conducir a soluciones más elegantes y, a veces, más eficientes que los métodos iterativos para problemas con subestructuras auto-similares.

## La Tarea

Implementa una función `recursive_min_max(arr: list[int]) -> tuple[int, int]` que encuentre tanto el elemento mínimo como el máximo en una lista de enteros utilizando recursión.

### Especificaciones

-   **Nombre de la Función**: `recursive_min_max`
-   **Argumentos**: `arr` (lista de enteros)
-   **Tipo de Retorno**: `tuple[int, int]`
-   **Resultado Esperado**: Una tupla que contenga el valor mínimo y máximo en la lista. Para una lista vacía, el comportamiento no está definido (asume una lista no vacía para simplificar, o maneja según se especifique).

### Restricciones

-   La lista contendrá enteros.
-   $1 \le 	ext{len(arr)} \le 10^5$

### Ejemplo

```python
>>> recursive_min_max([3, 1, 4, 1, 5, 9, 2, 6])
(1, 9)
>>> recursive_min_max([7])
(7, 7)
```

## Instrucciones

1.  Abre `exercises/recursive_min_max/solution.py`.
2.  Implementa la función `recursive_min_max`.
3.  Cambia `SUBMIT = False` a `SUBMIT = True` en la parte superior del archivo cuando estés listo para ser evaluado.
4.  Ejecuta `python solution.py` localmente para verificar tu solución con las pruebas integradas.
