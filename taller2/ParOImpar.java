import java.util.Scanner;
// Determinar si un número ingresado por teclado es par o impar


public class ParOImpar {
     // Variable de recoleccion de datos
    private static Scanner readScanner = new Scanner(System.in);

    // Metodo de identificación de datos positivo o negativo
public static String identificaNumeroParOImpar(Double num){
    if(num%2 == 0){
        return "El número ingresado es par.";
    }else if (num%2 != 0) {
        return "El número ingresado es impar.";
    }
    
    return "Ingreso un dato erroneo";
}

// Metodo de ejecución del proyecto
    public static void main(String[] args) {
        System.out.println("Ingrese un numero");
        Double num = readScanner.nextDouble();
        String resParImpar = identificaNumeroParOImpar(num);
        System.out.println(resParImpar);
    }
}

