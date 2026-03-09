# Ejercicio: Prueba de Primalidad

*[Read in English](README.md) | [Resolver en Línea](https://github.dev/matcom/gym/blob/main/exercises/prime_check/solution.py)*

## Antecedentes/Motivación

Un número primo es un número natural mayor que 1 que no tiene divisores positivos aparte de 1 y él mismo. Determinar si un número es primo es un problema fundamental en la teoría de números y tiene vastas aplicaciones en criptografía, como el algoritmo RSA. Aunque un enfoque ingenuo de probar todos los números hasta $n$ funciona, un método más eficiente es probar solo hasta $\sqrt{n}$, ya que cualquier factor mayor que la raíz cuadrada debe tener un factor correspondiente menor que ella.

## La Tarea

Implementa una función `prime_check(n: int) -> bool` que devuelva `True` si $n$ es primo y `False` en caso contrario.

### Especificaciones

- **Nombre de la Función**: `prime_check`
- **Argumentos**: `n` (int)
- **Tipo de Retorno**: `bool`
- **Resultado Esperado**: `True` si es primo, `False` en caso contrario.

### Restricciones

- $0 \le n \le 10^9$

### Ejemplo

```python
>>> prime_check(2)
True
>>> prime_check(4)
False
>>> prime_check(17)
True
```

## Instrucciones

1. Abre `exercises/prime_check/solution.py`.
2. Implementa la función `prime_check`.
3. Cambia `SUBMIT = False` a `SUBMIT = True` en la parte superior del archivo cuando estés listo para ser evaluado.
4. Ejecuta `python solution.py` localmente para verificar tu solución con las pruebas integradas.
