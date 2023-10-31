using System;

class Progarm
{
    static void Main()
    {
        int n = 5;
        int result = Factorial(n);
        Console.WriteLine(result);
    }

    static int Factorial(int n)
    {
        if (n <= 1)
            return 1;
        else
            return n * Factorial(n - 1);
    }
}



