# CD Manager (Ejercicio 6)

Este proyecto implementa un gestor de canciones para un CD de audio con límite de 80 minutos.

## Estructura

El archivo principal `cd_manager.py` contiene toda la lógica dividida por responsabilidades:

1. **Estructura y Parseo (Natividad)**: `parse_duration` convierte strings ("3:30") a floats.
2. **Lógica del CD (Jose Luis)**: `add_song`, `total_time` gestionan el límite de 80 min.
3. **Interfaz y Persistencia (Cami)**: CLI para añadir/listar y guardado en `cd_songs.json`.
4. **Tests (Cesar)**: Pruebas unitarias integradas compatible con `pytest`.

## Ejecución

### Interfaz de Línea de Comandos (CLI)

Para iniciar el programa:

```bash
python cd_manager.py
```

Sigue las instrucciones en pantalla para añadir canciones. La lista se guardará automáticamente en `cd_songs.json` al salir con la opción 4.
