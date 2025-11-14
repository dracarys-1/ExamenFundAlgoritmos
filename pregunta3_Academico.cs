using System;
using System.Globalization;

public class EstadoAcademico
{
    public static void Main(string[] args)
    {
        // Configuración regional para asegurar el uso del punto decimal
        CultureInfo.CurrentCulture = CultureInfo.InvariantCulture;
        string nombreEstudiante = "";
        do
        {
            Console.WriteLine("\n--- Nuevo Estudiante ---");
            Console.Write("1. Ingrese el nombre del estudiante: ");
            nombreEstudiante = Console.ReadLine().Trim();

            // 1. Control de Salida
            if (nombreEstudiante.Equals("FIN", StringComparison.OrdinalIgnoreCase))
            {
                Console.WriteLine("Saliendo del sistema...");
                break;
            }

            // 2. Leer las 3 notas parciales
            double nota1 = LeerNota("2. Ingrese la Nota 1 (0-20): ");
            double nota2 = LeerNota("3. Ingrese la Nota 2 (0-20): ");
            double nota3 = LeerNota("4. Ingrese la Nota 3 (0-20): ");

            // 3. Calcular el promedio
            double promedio = (nota1 + nota2 + nota3) / 3.0;
            string estadoAcademico = "";

            // 4. Determinar el estado académico
            if (promedio >= 15.0)
            {
                estadoAcademico = "APROBADO";
            }
            else if (promedio >= 11.0)
            {
                estadoAcademico = "RECUPERACIÓN";
            }
            else
            {
                estadoAcademico = "DESAPROBADO";
            }

            // 5. Mostrar mensaje personalizado
            Console.WriteLine("RESULTADO ACADÉMICO:");
            Console.WriteLine($"Hola {nombreEstudiante}, tu promedio final es: {promedio:F2}");
            Console.WriteLine($"Hola {nombreEstudiante}, tu estado es: {estadoAcademico}");

        } while (!nombreEstudiante.Equals("FIN", StringComparison.OrdinalIgnoreCase));
    }

    private static double LeerNota(string mensaje)
    {
        double nota = -1;
        while (nota < 0 || nota > 20)
        {
            Console.Write(mensaje);
            if (!double.TryParse(Console.ReadLine(), out nota) || nota < 0 || nota > 20)
            {
                Console.WriteLine("Error: Por favor, ingrese una nota numérica válida entre 0 y 20.");
                nota = -1; // Resetear la nota para mantener el bucle
            }
        }
        return nota;
    }
}