# Ejercicio 6 — CD de audio (80 minutos)
#
# En este archivo sólo debe haber una explicación de qué debe hacerse y cómo dividir
# la tarea entre 4 personas. NO incluir código aquí.
#
# Resumen del problema:
# - Mantener una lista de canciones con: nombre, artista y duración.
# - La suma de duraciones no debe superar 80 minutos (MAX_TIME = 80).
# - Cada canción debe almacenar la duración como número (minutos en float).
# - Añadir una canción debe validar el formato de la duración y sólo permitir la
#   inserción si la suma permanece <= 80 minutos.
#
# División de tareas para 4 personas:
#
# Natividad — Estructura y parseo
# - Definir claramente la estructura de una canción (p.ej. dict o dataclass).
# - Implementar `parse_duration(value)` que acepte:
#     * enteros/float (ej. 3, 3.5)
#     * strings con punto decimal (ej. "3.5")
#     * formato "mm:ss" (ej. "3:30" -> 3.5 minutos)
#   y devuelva la duración en minutos (float). Manejar errores con ValueError.
# - Escribir pruebas unitarias para distintos formatos aceptados e inválidos.
#
# Jose Luis — Lógica del CD (core)
# - Implementar las funciones principales:
#     * `add_song(name, artist, duration)` → True si añadió, False si no cupo.
#     * `total_time()` → suma actual en minutos.
#     * `can_add(duration)` → True/False.
#     * `clear_cd()` → limpiar la lista (útil para tests).
# - Asegurar que la lógica compare correctamente contra `MAX_TIME`.
# - Añadir tests para casos límite (exactamente 80, y justo por encima).
#
# Cami — Interfaz / Importación / CLI ( solo usa la consola pero que se vea bonito )
# - Crear una interfaz simple (CLI o funciones) para añadir/listar canciones
#   y mostrar tiempo total y tiempo restante.
# - Implementar import/export a JSON para persistir la lista de canciones.
# - Mensajes claros cuando una canción no cabe.
#
# Cesar — Tests y documentación 
# - Escribir tests `pytest` para parseo, `add_song`, y casos límite.
# - Añadir docstrings y un `README.md` que explique cómo ejecutar las pruebas
#   y usar la interfaz.
# - Verificar cobertura y revisar casos de borde (segundos fuera de rango,
#   entradas vacías, tipos incorrectos).
#
# Notas técnicas:
# - Preferir almacenar duración en minutos como `float` para la suma.
# - Evitar usar strings para la duración en la estructura guardada.
# - Tratar cuidadosamente la precisión: comparar con un pequeño tol (ej. 1e-9)
#   al verificar si cabe en el CD.
#
# Fin de la explicación.
