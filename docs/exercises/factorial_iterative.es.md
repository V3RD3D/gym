# Ejercicio: Factorial Iterativo

*[Read in English](README.md) | [Resolver en Línea](https://github.dev/matcom/gym/blob/main/exercises/factorial_iterative/solution.py)*

## Antecedentes/Motivación

El factorial de un número entero no negativo $n$, denotado por $n!$, es el producto de todos los enteros positivos menores o iguales que $n$. Los factoriales se utilizan en muchas áreas de las matemáticas, incluyendo la combinatoria, el álgebra y el análisis matemático. Calcular un factorial es un ejemplo clásico utilizado para enseñar la acumulación basada en bucles y a menudo se compara con su implementación recursiva.

## La Tarea

Implementa una función `factorial_iterative(n: int) -> int` que calcule el factorial de $n$ usando un bucle.

### Especificaciones

- **Nombre de la Función**: `factorial_iterative`
- **Argumentos**: `n` (int)
- **Tipo de Retorno**: `int`
- **Resultado Esperado**: El valor de $n!$. Para $n=0$, $0! = 1$.

### Restricciones

- $0 \le n \le 50$

### Ejemplo

```python
>>> factorial_iterative(0)
1
>>> factorial_iterative(5)
120
>>> factorial_iterative(10)
3628800
```

## Instrucciones

1. Abre `exercises/factorial_iterative/solution.py`.
2. Implementa la función `factorial_iterative`.
3. Cambia `SUBMIT = False` a `SUBMIT = True` en la parte superior del archivo cuando estés listo para ser evaluado.
4. Ejecuta `python solution.py` localmente para verificar tu solución con las pruebas integradas.
