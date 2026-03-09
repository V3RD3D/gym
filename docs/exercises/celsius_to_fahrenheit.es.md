# Ejercicio: Conversión de Temperatura

*[Read in English](README.md) | [Resolver en Línea](https://github.dev/matcom/gym/blob/main/exercises/celsius_to_fahrenheit/solution.py)*

## Antecedentes/Motivación

Convertir temperaturas entre diferentes escalas es una tarea fundamental en ciencia e ingeniería. La escala Celsius, comúnmente utilizada en la mayor parte del mundo, y la escala Fahrenheit, utilizada principalmente en los Estados Unidos, están relacionadas por una ecuación lineal. Implementar esta conversión es un ejercicio clásico para practicar la precedencia aritmética y las operaciones de punto flotante.

## La Tarea

Implementa una función `celsius_to_fahrenheit(celsius: float) -> float` que convierta una temperatura de Celsius a Fahrenheit usando la fórmula:
$$F = (C \times \frac{9}{5}) + 32$$

### Especificaciones

- **Nombre de la Función**: `celsius_to_fahrenheit`
- **Argumentos**: `celsius` (float)
- **Tipo de Retorno**: `float`
- **Resultado Esperado**: La temperatura convertida a Fahrenheit.

### Restricciones

- $-273.15 \le \text{celsius} \le 10^6$ (Cero absoluto hasta un valor muy alto)

### Ejemplo

```python
>>> celsius_to_fahrenheit(0)
32.0
>>> celsius_to_fahrenheit(100)
212.0
>>> celsius_to_fahrenheit(-40)
-40.0
```

## Instrucciones

1. Abre `exercises/celsius_to_fahrenheit/solution.py`.
2. Implementa la función `celsius_to_fahrenheit`.
3. Cambia `SUBMIT = False` a `SUBMIT = True` en la parte superior del archivo cuando estés listo para ser evaluado.
4. Ejecuta `python solution.py` localmente para verificar tu solución con las pruebas integradas.
