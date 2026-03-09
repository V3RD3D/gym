# Ejercicio: Mínimo/Máximo de una Lista

*[Read in English](README.md) | [Resolver en Línea](https://github.dev/matcom/gym/blob/main/exercises/min_max_list/solution.py)*

## Antecedentes/Motivación

Encontrar los elementos mínimo y máximo en una colección es una tarea fundamental. Aunque Python proporciona las funciones integradas `min()` y `max()`, implementarlo manualmente ayuda a entender cómo rastrear el estado a través de múltiples iteraciones. La eficiencia es clave: queremos encontrar ambos valores en una sola pasada por la lista.

## La Tarea

Escribe una función `min_max_list(items: list[int]) -> tuple[int, int] | None` que devuelva una tupla que contenga los valores mínimo y máximo encontrados en la lista.

### Especificaciones

- Devuelve una tupla `(valor_minimo, valor_maximo)`.
- Debes recorrer la lista **solo una vez**.
- Si la lista está vacía, devuelve `None`.
- NO utilices las funciones integradas `min()` o `max()`.

### Restricciones

- `0 <= len(items) <= 10,000`
- `-10^9 <= items[i] <= 10^9`

### Ejemplo

```python
>>> min_max_list([3, 1, 4, 1, 5, 9, 2, 6, 5])
(1, 9)
>>> min_max_list([10])
(10, 10)
>>> min_max_list([])
None
```

## Instrucciones

1. Abre `exercises/min_max_list/solution.py`.
2. Implementa la función.
3. Cambia `SUBMIT = False` a `SUBMIT = True` cuando estés listo.
4. Ejecuta `python solution.py` para verificar con las autopruebas integradas.
