using Microsoft.VisualStudio.TestTools.UnitTesting;

[TestClass]
public class IsPrimeTests
{
    public static bool IsPrime(int num)
    {
    if (num <= 1)
        return false;
    
    for (int i = 2; i * i <= num; i++)
    {
        if (num % i == 0)
            return false;
    }
    return true;
    }
    
    [TestMethod]
    public void IsPrime_ShouldReturnFalseForNegativeNumbers()
    {
        bool result = IsPrimeTests.IsPrime(-1);
        Assert.IsFalse(result);
    }

    [TestMethod]
    public void IsPrime_ShouldReturnFalseForZero()
    {
        bool result = IsPrimeTests.IsPrime(0);
        Assert.IsFalse(result);
    }

    [TestMethod]
    public void IsPrime_ShouldReturnFalseForOne()
    {
        bool result = IsPrimeTests.IsPrime(1);
        Assert.IsFalse(result);
    }

    [TestMethod]
    public void IsPrime_ShouldReturnFalseForCompositeNumbers()
    {
        bool result = IsPrimeTests.IsPrime(4);
        Assert.IsFalse(result);

        result = IsPrimeTests.IsPrime(6);
        Assert.IsFalse(result);

        result = IsPrimeTests.IsPrime(8);
        Assert.IsFalse(result);

        result = IsPrimeTests.IsPrime(9);
        Assert.IsFalse(result);

        result = IsPrimeTests.IsPrime(10);
        Assert.IsFalse(result);
    }

    [TestMethod]
    public void IsPrime_ShouldReturnTrueForPrimeNumbers()
    {
        bool result = IsPrimeTests.IsPrime(2);
        Assert.IsTrue(result);

        result = IsPrimeTests.IsPrime(3);
        Assert.IsTrue(result);

        result = IsPrimeTests.IsPrime(5);
        Assert.IsTrue(result);

        result = IsPrimeTests.IsPrime(7);
        Assert.IsTrue(result);

        result = IsPrimeTests.IsPrime(11);
        Assert.IsTrue(result);
    }
}
