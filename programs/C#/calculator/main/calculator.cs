using System;

class Calculator
{
    static double Add(double a, double b)
    {
        return a + b;
    }

    static double Subtract(double a, double b)
    {
        return a - b;
    }

    static double Multiply(double a, double b)
    {
        return a * b;
    }

    static double Divide(double a, double b)
    {
        if (b == 0)
        {
            throw new ArgumentException("Cannot divide by zero");
        }
        return a / b;
    }

    static void Main()
    {
        string operations = "+ <-- add \n- <-- subtract \n* <-- multiply \n/ <-- divide\n";
        bool running = true;

        while (running)
        {
            Console.Write("Enter your operation:\n" + operations + "> ");
            char operatorSymbol = Convert.ToChar(Console.ReadLine());
            Console.WriteLine();

            Console.Write("Enter the first variable: \n> ");
            double variableOne = Convert.ToDouble(Console.ReadLine());

            Console.Write("Enter the second variable: \n> ");
            double variableTwo = Convert.ToDouble(Console.ReadLine());

            switch (operatorSymbol)
            {
                case '+':
                    Console.WriteLine($"Result: {Add(variableOne, variableTwo)}\n");
                    break;
                case '-':
                    Console.WriteLine($"Result: {Subtract(variableOne, variableTwo)}\n");
                    break;
                case '*':
                    Console.WriteLine($"Result: {Multiply(variableOne, variableTwo)}\n");
                    break;
                case '/':
                    try
                    {
                        Console.WriteLine($"Result: {Divide(variableOne, variableTwo)}\n");
                    }
                    catch (ArgumentException ex)
                    {
                        Console.WriteLine($"Error: {ex.Message}\n");
                    }
                    break;
                default:
                    Console.WriteLine("You did not enter a valid operator...\n");
                    break;
            }
        }
    }
}