# Explicación Detallada de `cd_manager.py`

Este documento desglosa la sintaxis y "caracteres especiales" utilizados en el código de Python.

## 1. Las "Flechas" y Anotaciones de Tipo (Type Hints)

En Python, verás algo como esto:

```python
def parse_duration(value: Union[str, float, int]) -> float:
```

### `-> float` (La "flecha")

Esto **NO** es una función flecha (como en JavaScript). En Python 3, esto se llama **Type Hinting** (pista de tipo) para el valor de retorno.

- Significa: "Esta función va a devolver un número decimal (`float`)".
- Es solo informativo para programadores y herramientas; Python no obliga a cumplirlo en ejecución.

### `: Union[str, float, int]`

- Son los dos puntos `:` después de un argumento.
- Significa: "El parámetro `value` espera ser de uno de estos tipos: Texto, Decimal o Entero".

---

## 2. Caracteres Especiales en Cadenas (Strings)

### `f"Texto {variable}"` (F-Strings)

La `f` antes de las comillas activa el **formato rápido**. Permite meter variables directamente dentro de `{}`.

```python
print(f"Tiempo total: {total}")
```

### Formateo dentro de `{}`

Dentro de las llaves, puedes usar `:` para dar instrucciones de cómo mostrar el número.

#### `:.2f` (Decimales)

```python
f"{dur_val:.2f}"
```

- `.`: Punto decimal.
- `2`: Dos dígitos después del punto.
- `f`: Float (formato de punto fijo).
- **Resultado**: `3.5` se convierte en `"3.50"`. `3.5555` se convierte en `"3.56"`.

#### `:02d` (Relleno con ceros)

```python
f"{secs:02d}"
```

- `0`: Rellenar espacios vacíos con ceros.
- `2`: El número debe ocupar al menos 2 espacios.
- `d`: Decimal integer (entero).
- **Resultado**: Si segundos es `5`, se imprime `"05"`. Si es `10`, se imprime `"10"`.

#### `:<20` (Alineación)

```python
f"{'Nombre':<20}"
```

- `<`: Alinear a la **izquierda**.
- `20`: Ocupar un ancho fijo de **20 caracteres**.
- Sirve para hacer tablas ordenadas en la consola.

---

## 3. Estructuras de Datos

### `List[Dict[...]]`

```python
cd_songs: List[Dict[str, Union[str, float]]] = []
```

Esto define la estructura de nuestra "base de datos" en memoria:

1. `List`: Es una lista `[]`.
2. `Dict`: Cada elemento de la lista es un diccionario `{}`.
3. `str, Union[...]`: Las claves del diccionario son texto, y los valores pueden ser texto o números.

---

## 4. Comparaciones Especiales

### `1e-9` (Notación Científica)

```python
if total_time() + dur <= MAX_TIME + 1e-9:
```

- `1e-9` es igual a $1 \times 10^{-9}$ o `0.000000001`.
- Se usa como "margen de error" (tolerancia) porque las sumas de decimales en las computadoras a veces no son exactas (ej. `0.1 + 0.2` a veces da `0.30000000000000004`).

---

## 5. Bloques Especiales

### `try / except`

```python
try:
    minutes = float(parts[0])
except ValueError:
    raise ValueError(...)
```

- Intenta ejecutar el código del bloque `try`.
- Si ocurre un error específico (`ValueError`), no rompe el programa, sino que salta al bloque `except` para manejarlo elegantemente.

### `if __name__ == '__main__':`

```python
if __name__ == '__main__':
    main()
```

- Esta línea comprueba si el archivo se está ejecutando directamente (haciendo clic en él o por consola).
- Si este archivo fuera importado por otro (`import cd_manager`), el bloque `main()` **NO** se ejecutaría automáticamente. Esto permite reutilizar las funciones sin arrancar el programa.
