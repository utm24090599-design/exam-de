using System;

class Program
{
    static void Main(string[] args)
    {
        Console.WriteLine("Prueba de duración de canciones");

        double d1 = DurationParser.ParseDuration("3:30");
        double d2 = DurationParser.ParseDuration(2.5);

        Song song = new Song("Song 1", "Artist 1", d1);

        Console.WriteLine($"Canción: {song.Name}");
        Console.WriteLine($"Artista: {song.Artist}");
        Console.WriteLine($"Duración: {song.Duration} minutos");
    }
}


