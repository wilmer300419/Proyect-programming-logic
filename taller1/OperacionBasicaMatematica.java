
import java.util.Scanner;


class OperacionBasicaMatematica{

    public static void main(String[] args) {
        
        Scanner read = new Scanner(System.in);
        
        float num1;
        float num2;
        float result;
        int resp;

        resp = 1;

        while (resp != 0) {

            result=0f;
            
            System.out.println("Ingrese un numero: ");
            num1 = read.nextFloat();

            System.out.println("Ingrese otro numero: ");
            num2 = read.nextFloat();

            System.out.println("---------------------------------------");
            System.out.println("Ingrese el codigo de la operación que desea realziar: ");
            System.out.println("0. Salir");
            System.out.println("1. Suma");
            System.out.println("2. Resta");
            System.out.println("3. Multiplicación");
            System.out.println("4. División");
            System.out.println("5. Modulo");
            System.out.println("---------------------------------------");

            resp = read.nextInt();

            switch (resp) {
                case 0 -> System.out.println("Decidio salir del programa");
                case 1 -> {
                    result = num1 + num2;
                    System.out.println("El resultado de la suma es: "+ result);
                }
                case 2 -> {
                    result = num1 - num2;
                    System.out.println("El resultado de la resta es: "+ result);
                }
                case 3 -> {
                    result = num1 * num2;
                    System.out.println("El resultado de la multiplicación es: "+ result);
                }
                case 4 -> {
                    result = num1 / num2;
                    System.out.println("El resultado de división es: "+ result);
                }
                case 5 -> {
                    result = num1 % num2;
                    System.out.println("El resultado del modulo es: "+ result);
                }                                    
            
                default -> System.out.println("Ingresdo un valor erroneo");
            }
            
        }
        System.out.println("¡Gracias por usar nuestro programa!");
        
        read.close();

    }


}


