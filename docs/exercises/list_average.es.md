# Ejercicio: Calcular Promedio

*[Read in English](README.md) | [Resolver en Línea](https://github.dev/matcom/gym/blob/main/exercises/list_average/solution.py)*

## Antecedentes/Motivación

La media aritmética, a menudo llamada simplemente promedio, es una de las medidas estadísticas más comunes. Proporciona un valor central para un conjunto de números y se utiliza en todo, desde calificaciones escolares hasta investigación científica. En programación, calcular un promedio es un ejercicio fundamental para practicar el patrón acumulador y el manejo de colecciones de datos.

## La Tarea

Implementa una función `list_average(numbers: list[float]) -> float` que devuelva la media aritmética de una lista de números.

### Especificaciones

- **Nombre de la Función**: `list_average`
- **Argumentos**: `numbers` (lista de float)
- **Tipo de Retorno**: `float`
- **Resultado Esperado**: La suma de todos los elementos dividida por la cantidad de elementos. Si la lista está vacía, devuelve `0.0`.

### Restricciones

- $0 \le \text{len(numbers)} \le 10^5$
- Los números pueden ser enteros o flotantes.

### Ejemplo

```python
>>> list_average([1, 2, 3, 4, 5])
3.0
>>> list_average([10, 20, 30])
20.0
```

## Instrucciones

1. Abre `exercises/list_average/solution.py`.
2. Implementa la función `list_average`.
3. Cambia `SUBMIT = False` a `SUBMIT = True` en la parte superior del archivo cuando estés listo para ser evaluado.
4. Ejecuta `python solution.py` localmente para verificar tu solución con las pruebas integradas.
