using Xunit;
using System;

public class DurationParserTests
{
    [Fact]
    public void Parse_Int()
    {
        Assert.Equal(3.0, DurationParser.ParseDuration(3));
    }

    [Fact]
    public void Parse_Double()
    {
        Assert.Equal(3.5, DurationParser.ParseDuration(3.5));
    }

    [Fact]
    public void Parse_StringDecimal()
    {
        Assert.Equal(4.0, DurationParser.ParseDuration("4"));
        Assert.Equal(2.75, DurationParser.ParseDuration("2.75"));
    }

    [Fact]
    public void Parse_MmSs()
    {
        Assert.Equal(3.5, DurationParser.ParseDuration("3:30"));
        Assert.Equal(0.75, DurationParser.ParseDuration("0:45"));
    }

    [Fact]
    public void Parse_InvalidFormats()
    {
        Assert.Throws<ArgumentException>(() => DurationParser.ParseDuration("abc"));
        Assert.Throws<ArgumentException>(() => DurationParser.ParseDuration("3:75"));
        Assert.Throws<ArgumentException>(() => DurationParser.ParseDuration("-2"));
        Assert.Throws<ArgumentException>(() => DurationParser.ParseDuration(null));
    }
}
