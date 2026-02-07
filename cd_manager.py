"""
Módulo CD Manager - Ejercicio 6
Combina lógica de negocios, persistencia, interfaz CLI y pruebas unitarias.

Estructura:
- 1. Configuración y Estado Global
- 2. Natividad: Parseo y Estructura
- 3. Jose Luis: Lógica del CD
- 4. Cami: Persistencia e Interfaz (CLI)
- 5. Cesar: Tests (Pytest)
"""
import json
import os
import math
from typing import List, Dict, Union, Optional

# --- 1. CONFIGURACIÓN Y ESTADO GLOBAL ---
MAX_TIME: float = 80.0
DB_FILE: str = "cd_songs.json"

# Estructura de canción: Dict[str, Union[str, float]]
# Claves: "name" (str), "artist" (str), "duration" (float)
cd_songs: List[Dict[str, Union[str, float]]] = []

# --- 2. PARSEO Y ESTRUCTURA ---

def parse_duration(value: Union[str, float, int]) -> float:
    """
    Convierte un valor de entrada en minutos (float).
    
    Formatos aceptados:
    - Entero: 3 -> 3.0
    - Float: 3.5 -> 3.5
    - String numérico: "3.5" -> 3.5
    - String "mm:ss": "3:30" -> 3.5
    
    Lanza ValueError si el formato es inválido o si los segundos están fuera de rango (0-59).
    """
    if isinstance(value, (int, float)):
        val = float(value)
        if val < 0:
             raise ValueError("La duración no puede ser negativa.")
        return val

    if not isinstance(value, str):
        raise ValueError(f"Tipo no soportado: {type(value)}")

    s = value.strip()
    if not s:
        raise ValueError("Duración vacía")

    # Caso "mm:ss"
    if ":" in s:
        parts = s.split(":")
        if len(parts) != 2:
            raise ValueError("Formato 'mm:ss' incorrecto (demasiadas partes).")
        
        try:
            minutes = float(parts[0])
            seconds = float(parts[1])
        except ValueError:
            raise ValueError("Minutos o segundos no numéricos.")
            
        if not (0 <= seconds < 60):
            raise ValueError("Segundos deben estar entre 0 y 59.")
        
        if minutes < 0:
             raise ValueError("Minutos negativos no permitidos.")

        return minutes + (seconds / 60.0)

    # Caso número directo en string
    try:
        val = float(s)
        if val < 0:
            raise ValueError("La duración no puede ser negativa.")
        return val
    except ValueError:
        raise ValueError(f"Formato desconocido: {value}")


# --- 3. LÓGICA DEL CD (CORE) ---

def total_time() -> float:
    """Devuelve la suma total de duraciones en el CD."""
    return sum(song["duration"] for song in cd_songs)

def can_add(duration: float) -> bool:
    """Comprueba si cabe una canción de 'duration' minutos."""
    # Usamos tolerancia 1e-9 para comparaciones de float
    return (total_time() + duration) <= (MAX_TIME + 1e-9)

def add_song(name: str, artist: str, duration: Union[str, float, int]) -> bool:
    """
    Intenta añadir una canción.
    Retorna True si tuvo éxito, False si no cupo en el tiempo restante.
    """
    try:
        minutes = parse_duration(duration)
    except ValueError as e:
        print(f"Error al parsear duración: {e}")
        return False

    if can_add(minutes):
        song = {
            "name": name,
            "artist": artist,
            "duration": minutes
        }
        cd_songs.append(song)
        return True
    else:
        return False

def clear_cd() -> None:
    """Limpia la lista de canciones. Útil para tests CLI."""
    cd_songs.clear()


# --- 4. PERSISTENCIA E INTERFAZ (CLI) ---

def save_songs():
    """Guarda la lista actual en JSON."""
    try:
        with open(DB_FILE, 'w', encoding='utf-8') as f:
            json.dump(cd_songs, f, indent=4)
        print(f"Canciones guardadas en {DB_FILE}")
    except IOError as e:
        print(f"Error guardando archivo: {e}")

def load_songs():
    """Carga las canciones desde JSON si existe."""
    if not os.path.exists(DB_FILE):
        return
    try:
        with open(DB_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
            if isinstance(data, list):
                # Validamos sanity básica
                clear_cd()
                for s in data:
                    cd_songs.append(s)
        print(f"Cargadas {len(cd_songs)} canciones de {DB_FILE}")
    except (json.JSONDecodeError, IOError) as e:
        print(f"Error cargando archivo: {e}")

def format_time(minutes: float) -> str:
    """Helper para mostrar minutos como mm:ss."""
    mins = int(minutes)
    secs = int((minutes - mins) * 60)
    return f"{mins}:{secs:02d}"

def cli_add_song():
    print("\n--- AÑADIR CANCIÓN ---")
    name = input("Nombre de la canción: ").strip()
    if not name:
        print("El nombre no puede estar vacío.")
        return
    artist = input("Artista: ").strip()
    duration_input = input("Duración (mm:ss o min): ").strip()

    # Validamos primero parseo para dar feedback rápido
    try:
        dur_val = parse_duration(duration_input)
    except ValueError as e:
        print(f"❌ Error de formato: {e}")
        return

    if add_song(name, artist, dur_val):
        print(f"✅ '{name}' añadida correctamente.")
        print(f"Tiempo total: {format_time(total_time())} / {MAX_TIME} min")
    else:
        rem = MAX_TIME - total_time()
        print(f"⚠️ No cabe en el CD.")
        print(f"Necesitas {dur_val:.2f} min, pero solo quedan {rem:.2f} min libres.")

def cli_list_songs():
    print(f"\n--- LISTA DE CANCIONES ({len(cd_songs)}) ---")
    print(f"{'#':<3} | {'Nombre':<20} | {'Artista':<15} | {'Duración'}")
    print("-" * 50)
    for i, song in enumerate(cd_songs, 1):
        dur_str = format_time(song['duration'])
        print(f"{i:<3} | {song['name']:<20} | {song['artist']:<15} | {dur_str}")
    
    total = total_time()
    print("-" * 50)
    print(f"Tiempo Total: {format_time(total)} ({total:.2f} min)")
    print(f"Tiempo Restante: {format_time(MAX_TIME - total)}")

def main():
    load_songs()
    
    # Verificación inicial al arrancar
    start_total = total_time()
    if start_total > MAX_TIME:
        print(f"ATENCIÓN: Cuidado, las canciones cargadas ({format_time(start_total)}) EXCEDEN el límite de {MAX_TIME} min.")
    
    while start_total < MAX_TIME:
        current_total = total_time()
        remaining = MAX_TIME - current_total
        
        print(f"\n=== CD MANAGER (80 MIN) ===")
        print(f"Tiempo usado: {format_time(current_total)} | Restante: {format_time(remaining)}")
        print("1. Añadir canción")
        print("2. Listar canciones")
        print("3. Limpiar CD")
        print("4. Guardar y Salir")
        
        opc = input("Opción: ").strip()
        
        if opc == '1':
            if remaining <= 1e-9:
                print("\n ¡El CD ya está lleno! No puedes añadir más canciones.")
            else:
                cli_add_song()
        elif opc == '2':
            cli_list_songs()
        elif opc == '3':
            confirm = input("¿Seguro que quieres borrar todo? (s/n): ")
            if confirm.lower() == 's':
                clear_cd()
                print("CD limpiado.")
        elif opc == '4':
            save_songs()
            print("Adiós!")
            break
        else:
            print("Opción inválida.")

if __name__ == '__main__':
    # Si se ejecuta directamente, corremos la CLI
    main()