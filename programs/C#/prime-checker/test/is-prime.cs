
using Microsoft.VisualStudio.TestTools.UnitTesting;

[TestClass]
public class IsPrimeTests
{
    [TestMethod]
    public void IsPrime_ShouldReturnFalseForNegativeNumbers()
    {
        bool result = Program.IsPrime(-1);
        Assert.IsFalse(result);
    }

    [TestMethod]
    public void IsPrime_ShouldReturnFalseForZero()
    {
        bool result = Program.IsPrime(0);
        Assert.IsFalse(result);
    }

    [TestMethod]
    public void IsPrime_ShouldReturnFalseForOne()
    {
        bool result = Program.IsPrime(1);
        Assert.IsFalse(result);
    }

    [TestMethod]
    public void IsPrime_ShouldReturnFalseForCompositeNumbers()
    {
        bool result = Program.IsPrime(4);
        Assert.IsFalse(result);

        result = Program.IsPrime(6);
        Assert.IsFalse(result);

        result = Program.IsPrime(8);
        Assert.IsFalse(result);

        result = Program.IsPrime(9);
        Assert.IsFalse(result);

        result = Program.IsPrime(10);
        Assert.IsFalse(result);
    }

    [TestMethod]
    public void IsPrime_ShouldReturnTrueForPrimeNumbers()
    {
        bool result = Program.IsPrime(2);
        Assert.IsTrue(result);

        result = Program.IsPrime(3);
        Assert.IsTrue(result);

        result = Program.IsPrime(5);
        Assert.IsTrue(result);

        result = Program.IsPrime(7);
        Assert.IsTrue(result);

        result = Program.IsPrime(11);
        Assert.IsTrue(result);
    }
}
