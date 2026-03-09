# Ejercicio: Inversión de Caso

*[Read in English](README.md) | [Solve Online](https://github.dev/matcom/gym/blob/main/exercises/case_inverter/solution.py)*

## Antecedentes/Motivación

Los datos de texto a menudo vienen con mayúsculas y minúsculas inconsistentes. Poder invertir el caso de los caracteres (convertir minúsculas a mayúsculas y viceversa) es una tarea común de manipulación de cadenas con aplicaciones en la limpieza de datos, el procesamiento de texto y la validación de la entrada del usuario.

## La Tarea

Implementa una función `case_inverter(s: str) -> str` que tome una cadena y devuelva una nueva cadena con el caso de cada carácter invertido.

### Especificaciones

-   **Nombre de la Función**: `case_inverter`
-   **Argumentos**: `s` (str)
-   **Tipo de Retorno**: `str`
-   **Resultado Esperado**: Una nueva cadena con el caso de cada carácter invertido.

### Restricciones

-   La cadena de entrada puede contener letras, números, espacios y símbolos.

### Ejemplo

```python
>>> case_inverter("Hello World!")
"hELLO wORLD!"
>>> case_inverter("Python 3.12")
"pYTHON 3.12"
```

## Instrucciones

1.  Abre `exercises/case_inverter/solution.py`.
2.  Implementa la función `case_inverter`.
3.  Cambia `SUBMIT = False` a `SUBMIT = True` en la parte superior del archivo cuando estés listo para ser evaluado.
4.  Ejecuta `python solution.py` localmente para verificar tu solución con las pruebas integradas.
