
using System;
using NUnit.Framework;

[TestFixture]
public class CalculatorTests
{
    [Test]
    public void Add_ValidInputs_ReturnsSum()
    {
        // Arrange
        double a = 5;
        double b = 3;
        double expectedResult = 8;

        // Act
        double result = Calculator.Add(a, b);

        // Assert
        Assert.AreEqual(expectedResult, result);
    }

    [Test]
    public void Subtract_ValidInputs_ReturnsDifference()
    {
        // Arrange
        double a = 10;
        double b = 4;
        double expectedResult = 6;

        // Act
        double result = Calculator.Subtract(a, b);

        // Assert
        Assert.AreEqual(expectedResult, result);
    }

    [Test]
    public void Multiply_ValidInputs_ReturnsProduct()
    {
        // Arrange
        double a = 7;
        double b = 2;
        double expectedResult = 14;

        // Act
        double result = Calculator.Multiply(a, b);

        // Assert
        Assert.AreEqual(expectedResult, result);
    }

    [Test]
    public void Divide_ValidInputs_ReturnsQuotient()
    {
        // Arrange
        double a = 15;
        double b = 5;
        double expectedResult = 3;

        // Act
        double result = Calculator.Divide(a, b);

        // Assert
        Assert.AreEqual(expectedResult, result);
    }

    [Test]
    public void Divide_DivideByZero_ThrowsArgumentException()
    {
        // Arrange
        double a = 10;
        double b = 0;

        // Act + Assert
        Assert.Throws<ArgumentException>(() => Calculator.Divide(a, b));
    }
}
