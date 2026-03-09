# Fibonacci Recursivo de Cola

## Conocimientos Previos
La secuencia de Fibonacci se define recursivamente como $F(n) = F(n-1) + F(n-2)$, con $F(0) = 0$ y $F(1) = 1$. La solución recursiva estándar se ramifica exponencialmente (complejidad temporal $O(2^n)$), lo cual es muy ineficiente. Usando recursión de cola, podemos pasar los dos valores anteriores hacia adelante como estado, optimizando la complejidad temporal a $O(n)$.

## Tarea
Calcula el $n$-ésimo número de Fibonacci usando una función recursiva de cola.

## Especificaciones
- **Entrada:** Un número entero `n` ($n \ge 0$).
- **Salida:** El $n$-ésimo número de Fibonacci.

## Restricciones
- La función debe ser recursiva.
- La llamada recursiva debe ser la última operación de la función.
- No uses bucles iterativos.
- Debes usar argumentos acumuladores para realizar el seguimiento del estado.

## Ejemplo
```python
>>> fibonacci_tail(5)
5
>>> fibonacci_tail(10)
55
```

## Instrucciones
1. Implementa la función `fibonacci_tail` usando recursión de cola.
2. Inicializa dos acumuladores (`a` y `b`) para rastrear los dos valores anteriores de la secuencia.
3. Valida tu código con las pruebas provistas.

[Resuélvelo en línea](https://github.dev/matcom/gym/blob/main/exercises/fibonacci_tail/solution.py), | [Read in English](README.md)
