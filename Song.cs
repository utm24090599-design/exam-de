public class Song
{
    public string Name { get; set; } // Nombre de la canción
    public string Artist { get; set; } // Artistas
    public double Duration { get; set; } // Minutos

    public Song(string name, string artist, double duration)
    {
        Name = name;
        Artist = artist;
        Duration = duration;
    }
}

