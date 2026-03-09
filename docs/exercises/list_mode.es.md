# Ejercicio: Elemento más Frecuente

*[Read in English](README.md) | [Resolver en Línea](https://github.dev/matcom/gym/blob/main/exercises/list_mode/solution.py)*

## Antecedentes/Motivación

En estadística, la moda es el valor que aparece con más frecuencia en un conjunto de datos. Encontrar la moda es una aplicación práctica del conteo de frecuencias, que es una tarea común en el análisis de datos, el procesamiento del lenguaje natural y muchos otros campos. En Python, esto se resuelve típicamente usando un diccionario para mapear cada elemento a su conteo de ocurrencias.

## La Tarea

Implementa una función `list_mode(items: list[Any]) -> Any` que devuelva el elemento más frecuente en una lista. Si la lista está vacía, devuelve `None`. Si hay un empate entre varios elementos, puedes devolver cualquiera de ellos.

### Especificaciones

- **Nombre de la Función**: `list_mode`
- **Argumentos**: `items` (lista de cualquier tipo)
- **Tipo de Retorno**: `Any` (el elemento más frecuente)
- **Resultado Esperado**: El elemento con la mayor frecuencia.

### Restricciones

- $0 \le \text{len(items)} \le 10^5$
- Los elementos pueden ser de cualquier tipo "hashable" (enteros, cadenas, etc.).

### Ejemplo

```python
>>> list_mode([1, 2, 2, 3, 3, 3])
3
>>> list_mode(['a', 'b', 'a'])
'a'
```

## Instrucciones

1. Abre `exercises/list_mode/solution.py`.
2. Implementa la función `list_mode`.
3. Cambia `SUBMIT = False` a `SUBMIT = True` en la parte superior del archivo cuando estés listo para ser evaluado.
4. Ejecuta `python solution.py` localmente para verificar tu solución con las pruebas integradas.
