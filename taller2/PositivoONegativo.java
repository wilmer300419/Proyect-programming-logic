
import java.util.Scanner;
// Pedirle al usuario que ingrese un numero e indicar si es positivo o negativo


public class PositivoONegativo{

    // Variable de recoleccion de datos
    private static Scanner readScanner = new Scanner(System.in);

    // Metodo de identificación de datos positivo o negativo
public static String identificaNumeroPositivoONegativo(Double num){
    if(num>0){
        return "El número ingresado es positivo.";
    }else if (num<0) {
        return "El número ingresado es negativo.";
    }else if (num == 0){
        return "El número ingresado es 0.";
    }
    
    return "Ingreso un dato diferente a un número";
}

// Metodo de ejecución del proyecto
    public static void main(String[] args) {
        System.out.println("Ingrese un numero");
        Double num = readScanner.nextDouble();
        String resPositNegat = identificaNumeroPositivoONegativo(num);
        System.out.println(resPositNegat);
    }
}