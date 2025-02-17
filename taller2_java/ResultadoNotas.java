/// 4. Realizar un programa que capture 5 notas por cada corte, son dos cortes, 
// calcula su promedio y se acumula respecto a cada corte, el primer corte vale el 
// 40% y el segundo vale el 60% y se deberá dar la nota final si aprobó o reprobó
// Sabiendo que se pasa con 2.95 a 5.0 y se pierde con 2.94 a 0 

import java.util.Scanner;

public class ResultadoNotas {
    private static Scanner readScanner = new Scanner(System.in);

    //Método de capturar notas
    private static double capturarNotas(int corte) {
        System.out.println("Por favor, ingrese las 5 notas del corte " + corte + ":");
        double sumaNotas = 0;
        for (int i = 0; i < 5; i++) {
            double nota;
            do {
                System.out.print("Nota " + (i + 1) + " (entre 0 y 5): ");
                nota = readScanner.nextDouble();
                if (nota < 0 || nota > 5) {
                    System.out.println("Error: La nota debe estar entre 0 y 5.");
                }
            } while (nota < 0 || nota > 5);
            sumaNotas += nota;
        }
        return sumaNotas / 5;
    }

    // Método de ejecución del proyecto
    public static void main(String[] args) {
        double promedioCorte1 = capturarNotas(1) * 0.4;
        double promedioCorte2 = capturarNotas(2) * 0.6;
        double notaFinal = promedioCorte1 + promedioCorte2;

        System.out.println("Nota final: " + notaFinal);
        if (notaFinal >= 2.95) {
            System.out.println("¡Aprobaste!");
        } else {
            System.out.println("Reprobaste.");
        }
    }
        
}
