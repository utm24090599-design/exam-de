from dataclasses import dataclass

@dataclass
class Song:
    name: str        #Nombre de la canción
    artist: str      #Nombre del artista
    duration: float  #Minutos

def parse_duration(value):
    #Número directo
    if isinstance(value, (int, float)):
        if value <= 0:
            raise ValueError("La duración debe ser positiva")
        return float(value)

    if isinstance(value, str):
        value = value.strip()

        #Formato mm:ss
        if ":" in value:
            try:
                minutes, seconds = value.split(":")
                minutes = int(minutes)
                seconds = int(seconds)

                if minutes < 0 or not (0 <= seconds < 60):
                    raise ValueError

                return minutes + seconds / 60
            except Exception:
                raise ValueError("Formato mm:ss inválido")

        #Decimal
        try:
            duration = float(value)
            if duration <= 0:
                raise ValueError
            return duration
        except Exception:
            raise ValueError("Formato de duración inválido")

    raise ValueError("Tipo de dato no soportado")

import unittest

class TestParseDuration(unittest.TestCase):

    # Formatos válidos
    def test_int(self):
        self.assertEqual(parse_duration(3), 3.0)

    def test_float(self):
        self.assertEqual(parse_duration(3.5), 3.5)

    def test_string_decimal(self):
        self.assertEqual(parse_duration("4.25"), 4.25)

    def test_mm_ss(self):
        self.assertEqual(parse_duration("3:30"), 3.5)

    def test_mm_ss_exact(self):
        self.assertEqual(parse_duration("5:00"), 5.0)

    # Formatos inválidos
    def test_negative(self):
        with self.assertRaises(ValueError):
            parse_duration(-3)

    def test_bad_string(self):
        with self.assertRaises(ValueError):
            parse_duration("abc")

    def test_bad_mm_ss(self):
        with self.assertRaises(ValueError):
            parse_duration("3:75")

    def test_empty(self):
        with self.assertRaises(ValueError):
            parse_duration("")

if __name__ == "__main__":
    unittest.main()
