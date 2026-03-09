# Ejercicio: Saludo Personalizado

*[Read in English](README.md) | [Resolver en Línea](https://github.dev/matcom/gym/blob/main/exercises/personalized_greeting/solution.py)*

## Antecedentes/Motivación

Interactuar con los usuarios a menudo implica formatear cadenas para incluir información personal. Las f-strings de Python proporcionan una forma potente y legible de realizar la interpolación de cadenas. En este ejercicio, practicarás el uso de f-strings con múltiples variables.

## La Tarea

Escribe una función `personalized_greeting(name, age)` que tome un nombre (cadena) y una edad (entero) y devuelva una cadena de saludo en el formato: `"Hello {name}, you are {age} years old"`.

### Especificaciones

- **Nombre de la Función**: `personalized_greeting`
- **Argumentos**:
    - `name` (str): El nombre de la persona.
    - `age` (int): La edad de la persona.
- **Valor de Retorno**:
    - `str`: El saludo formateado.

### Restricciones

- `name` será una cadena no vacía.
- `age` será un entero positivo.

### Ejemplo

```python
>>> personalized_greeting("Alice", 25)
'Hello Alice, you are 25 years old'
```

## Instrucciones

1. Abre `exercises/personalized_greeting/solution.py`.
2. Implementa la función.
3. Cambia `SUBMIT = False` a `SUBMIT = True` cuando estés listo.
4. Ejecuta `python solution.py` para verificar con las pruebas integradas.
