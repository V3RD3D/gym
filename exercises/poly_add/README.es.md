# Suma de Polinomios

## Contexto
La suma de polinomios implica sumar los coeficientes de los términos del mismo grado. Si los polinomios tienen grados diferentes, los términos de mayor grado faltantes se pueden tratar como si tuvieran un coeficiente de 0.

## Tarea
Escribe una función `poly_add(poly1, poly2)` que devuelva la suma de dos polinomios. Ambos polinomios se dan como listas de coeficientes de mayor a menor grado.

## Especificaciones
- La función toma dos listas de coeficientes `poly1` y `poly2`.
- Debe devolver una nueva lista que represente la suma de los polinomios.
- La lista resultante no debe tener ceros a la izquierda a menos que el polinomio sea exactamente 0.

## Restricciones
- `poly1` y `poly2` no estarán vacíos.
- La salida debe estar normalizada para no tener ceros iniciales innecesarios.

## Ejemplo
```python
>>> poly_add([3, 0, 4], [1, 5])
[3, 1, 9]
```

## Instrucciones
1. Implementa la lógica en `solution.py`.
2. No uses `input()` ni `print()`.
3. Prueba tu solución localmente antes de enviarla.

[Resolver en Línea](https://github.dev/matcom/gym/blob/main/exercises/poly_add/solution.py) | [View in English](./README.md), | [Read in English](README.md)
