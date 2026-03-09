# Ejercicio: Suma Recursiva de Lista

*[Read in English](README.md) | [Solve Online](https://github.dev/matcom/gym/blob/main/exercises/sum_list_recursive/solution.py)*

## Antecedentes/Motivación

La recursión es un método para resolver un problema computacional donde la solución depende de las soluciones a instancias más pequeñas del mismo problema. Para estructuras de datos lineales como las listas, el paso recursivo suele implicar separar el primer elemento (la cabeza) del resto de la lista (la cola) y aplicar la función a la cola. Este enfoque ayuda a comprender las estrategias de divide y vencerás y puede conducir a soluciones elegantes para ciertos problemas.

## La Tarea

Implementa una función `sum_list_recursive(lst: list[int]) -> int` que calcule la suma de todos los elementos de una lista utilizando recursión.

### Especificaciones

-   **Nombre de la Función**: `sum_list_recursive`
-   **Argumentos**: `lst` (lista de enteros)
-   **Tipo de Retorno**: `int`
-   **Resultado Esperado**: La suma de todos los elementos de la lista. Para una lista vacía, la suma es 0.

### Restricciones

- La lista puede contener enteros.
- La longitud de la lista puede ser hasta $10^5$.

### Ejemplo

```python
>>> sum_list_recursive([1, 2, 3, 4])
10
>>> sum_list_recursive([])
0
```

## Instrucciones

1.  Abre `exercises/sum_list_recursive/solution.py`.
2.  Implementa la función `sum_list_recursive`.
3.  Cambia `SUBMIT = False` a `SUBMIT = True` en la parte superior del archivo cuando estés listo para ser evaluado.
4.  Ejecuta `python solution.py` localmente para verificar tu solución con las pruebas integradas.
