# Ejercicio: Calculadora de Interés Simple

*[Read in English](README.md) | [Resolver en Línea](https://github.dev/matcom/gym/blob/main/exercises/simple_interest/solution.py)*

## Antecedentes/Motivación

El interés simple es un método rápido y fácil para calcular el cargo por intereses en un préstamo. El interés simple se determina multiplicando la tasa de interés diaria por el capital por el número de días que transcurren entre pagos. Se utiliza comúnmente en préstamos a corto plazo y aplicaciones financieras simples.

## La Tarea

Implementa una función `simple_interest(principal: float, rate: float, time: float) -> float` que calcule el interés simple usando la fórmula:
$$I = \frac{P \times R \times T}{100}$$
donde:
- $P$ es el Capital (Principal).
- $R$ es la Tasa de interés anual (en porcentaje).
- $T$ es el Tiempo (en años).

### Especificaciones

- **Nombre de la Función**: `simple_interest`
- **Argumentos**: `principal` (float), `rate` (float), `time` (float)
- **Tipo de Retorno**: `float`
- **Resultado Esperado**: El interés simple calculado.

### Restricciones

- $0 \le \text{principal}, \text{rate}, \text{time} \le 10^9$

### Ejemplo

```python
>>> simple_interest(1000, 5, 2)
100.0
>>> simple_interest(500, 3.5, 1)
17.5
```

## Instrucciones

1. Abre `exercises/simple_interest/solution.py`.
2. Implementa la función `simple_interest`.
3. Cambia `SUBMIT = False` a `SUBMIT = True` en la parte superior del archivo cuando estés listo para ser evaluado.
4. Ejecuta `python solution.py` localmente para verificar tu solución con las pruebas integradas.
