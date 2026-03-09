# Ejercicio: Sumas Acumuladas

*[Read in English](README.md) | [Resolver en Línea](https://github.dev/matcom/gym/blob/main/exercises/prefix_sums/solution.py)*

## Antecedentes/Motivación

Una suma acumulada (también conocida como suma de prefijos) es una secuencia de sumas parciales de una secuencia dada. Por ejemplo, las sumas acumuladas de la secuencia $\{a, b, c, \dots\}$ son $\{a, a+b, a+b+c, \dots\}$. Esta es una técnica fundamental utilizada en programación competitiva y análisis de datos para calcular rápidamente la suma de cualquier sub-rango de una lista en tiempo $O(1)$ después de un paso de preprocesamiento de tiempo $O(n)$.

## La Tarea

Implementa una función `prefix_sums(numbers: list[int]) -> list[int]` que reciba una lista de enteros y devuelva una nueva lista donde cada elemento en el índice $i$ sea la suma de todos los elementos de la lista original desde el índice $0$ hasta el $i$.

### Especificaciones

- **Nombre de la Función**: `prefix_sums`
- **Argumentos**: `numbers` (lista de enteros)
- **Tipo de Retorno**: `list[int]`
- **Resultado Esperado**: Una lista de la misma longitud que contenga las sumas acumuladas.

### Restricciones

- $0 \le \text{len(numbers)} \le 10^5$
- Los elementos son enteros en el rango $[-10^9, 10^9]$.

### Ejemplo

```python
>>> prefix_sums([1, 2, 3])
[1, 3, 6]
>>> prefix_sums([10, -10, 5])
[10, 0, 5]
```

## Instrucciones

1. Abre `exercises/prefix_sums/solution.py`.
2. Implementa la función `prefix_sums`.
3. Cambia `SUBMIT = False` a `SUBMIT = True` en la parte superior del archivo cuando estés listo para ser evaluado.
4. Ejecuta `python solution.py` localmente para verificar tu solución con las pruebas integradas.
