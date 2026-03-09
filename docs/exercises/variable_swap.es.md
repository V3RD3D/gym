# Ejercicio: Intercambio de Variables

*[Read in English](README.md) | [Resolver en Línea](https://github.dev/matcom/gym/blob/main/exercises/variable_swap/solution.py)*

## Antecedentes/Motivación

En muchos algoritmos, es necesario intercambiar los valores de dos variables. En muchos lenguajes de programación, esto requiere una tercera variable temporal para guardar un valor mientras el otro es sobrescrito. Sin embargo, Python proporciona una forma elegante y concisa de hacer esto usando el desempaquetado de tuplas. Este ejercicio explora tanto la lógica del intercambio como la forma "Pythonic" de implementarlo.

## La Tarea

Implementa una función `variable_swap(a: any, b: any) -> tuple[any, any]` que reciba dos valores y los devuelva intercambiados en una tupla.

### Especificaciones

- **Nombre de la Función**: `variable_swap`
- **Argumentos**: `a` (cualquiera), `b` (cualquiera)
- **Tipo de Retorno**: `tuple[any, any]`
- **Resultado Esperado**: Una tupla `(b, a)`.

### Restricciones

- Los argumentos pueden ser de cualquier tipo de dato.

### Ejemplo

```python
>>> variable_swap(5, 10)
(10, 5)
>>> variable_swap("apple", "banana")
('banana', 'apple')
```

## Instrucciones

1. Abre `exercises/variable_swap/solution.py`.
2. Implementa la función `variable_swap`.
3. Cambia `SUBMIT = False` a `SUBMIT = True` en la parte superior del archivo cuando estés listo para ser evaluado.
4. Ejecuta `python solution.py` localmente para verificar tu solución con las pruebas integradas.
