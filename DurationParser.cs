using System;
using System.Globalization;

public static class DurationParser
{
    public static double ParseDuration(object value)
    {
        if (value == null)
            throw new ArgumentException("La duración no puede ser null");

        if (value is int i)
        {
            ValidatePositive(i);
            return i;
        }

        if (value is double d)
        {
            ValidatePositive(d);
            return d;
        }

        if (value is string s)
        {
            s = s.Trim();

            if (string.IsNullOrEmpty(s))
                throw new ArgumentException("La duración no puede estar vacía");

            // Formato mm:ss
            if (s.Contains(":"))
            {
                return ParseMinutesSeconds(s);
            }

            // Formato decimal
            if (double.TryParse(
                s,
                NumberStyles.Float,
                CultureInfo.InvariantCulture,
                out double result))
            {
                ValidatePositive(result);
                return result;
            }

            throw new ArgumentException($"Formato de duración inválido: {s}");
        }

        throw new ArgumentException($"Tipo no soportado: {value.GetType()}");
    }

    private static double ParseMinutesSeconds(string value)
    {
        var parts = value.Split(':');

        if (parts.Length != 2)
            throw new ArgumentException($"Formato mm:ss inválido: {value}");

        if (!int.TryParse(parts[0], out int minutes) ||
            !int.TryParse(parts[1], out int seconds))
            throw new ArgumentException($"Formato mm:ss inválido: {value}");

        if (minutes < 0 || seconds < 0 || seconds >= 60)
            throw new ArgumentException($"Valores fuera de rango: {value}");

        return minutes + (seconds / 60.0);
    }

    private static void ValidatePositive(double value)
    {
        if (value <= 0)
            throw new ArgumentException("La duración debe ser mayor a 0");
    }
}
