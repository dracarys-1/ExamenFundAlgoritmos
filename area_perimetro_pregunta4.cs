using System;

class Program
{
    static void Main()
    {
        int op;
        double x, b, h, r, area, perimetro;
        string resultado;

        do
        {
            Console.WriteLine("1 Cuadrado   2 Rectangulo   3 Circulo   4 Salir");
            Console.Write("Opcion: ");
            op = int.Parse(Console.ReadLine());

            switch (op)
            {
                case 1:
                    Console.Write("Lado: ");
                    x = double.Parse(Console.ReadLine());
                    area = x * x;
                    perimetro = 4 * x;
                    resultado = "A: " + Math.Round(area, 2) + "  P: " + Math.Round(perimetro, 2);
                    Console.WriteLine(resultado);
                    break;

                case 2:
                    Console.Write("Base: ");
                    b = double.Parse(Console.ReadLine());
                    Console.Write("Altura: ");
                    h = double.Parse(Console.ReadLine());
                    area = b * h;
                    perimetro = 2 * (b + h);
                    resultado = "A: " + Math.Round(area, 2) + "  P: " + Math.Round(perimetro, 2);
                    Console.WriteLine(resultado);
                    break;

                case 3:
                    Console.Write("Radio: ");
                    r = double.Parse(Console.ReadLine());
                    area = 3.14159265 * r * r;
                    perimetro = 2 * 3.14159265 * r;
                    resultado = "A: " + Math.Round(area, 2) + "  P: " + Math.Round(perimetro, 2);
                    Console.WriteLine(resultado);
                    break;

                case 4:
                    Console.WriteLine("Fin");
                    break;

                default:
                    Console.WriteLine("Opcion invalida");
                    break;
            }
            Console.WriteLine();

        } while (op != 4);
    }
}