# Evaluar Polinomio

## Contexto
El método de Horner es un algoritmo eficiente para evaluar polinomios. Reduce el número de multiplicaciones necesarias, transformando un polinomio de grado $n$ en una forma anidada.

## Tarea
Escribe una función `poly_evaluate(poly, x)` que evalúe un polinomio en un valor dado $x$. El polinomio se representa mediante una lista de sus coeficientes, desde el término de mayor grado hasta el término constante.

## Especificaciones
- La función toma una lista de coeficientes `poly` y un valor `x`.
- Debe devolver el polinomio evaluado como un número.
- Debe implementar el método de Horner eficientemente.

## Restricciones
- La lista `poly` tendrá al menos un elemento.
- Todos los elementos en `poly` y `x` serán números.

## Ejemplo
```python
>>> poly_evaluate([2, -6, 2, -1], 3)
5
```

## Instrucciones
1. Implementa la lógica en `solution.py`.
2. No uses `input()` ni `print()`.
3. Prueba tu solución localmente antes de enviarla.

[Resolver en Línea](https://github.dev/matcom/gym/blob/main/exercises/poly_evaluate/solution.py) | [View in English](./README.md), | [Read in English](README.md)
