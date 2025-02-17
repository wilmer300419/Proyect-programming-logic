import java.util.Scanner;

// 3. Crear una tienda, si el comprador gasta mas de $100 aplicar un 10% de 
// descuento, si su compra es de $150 de 15%, si es entre 160 y 200 el 20%, si es 
// mayor a 200 darle el 30% y un regalo.

public class Tienda {
      // Variable de recoleccion de datos
    private static Scanner readScanner = new Scanner(System.in);

    // Método de comprobación de descuento
    public static  String comprobarDescuento(Double valorDeCompra){

        Double resultadoDescuento;
        if (valorDeCompra <= 0) {
            return "El valor de la compra no puede ser negativo o cero";
        }

        if (valorDeCompra > 200) {
            resultadoDescuento = valorDeCompra - valorDeCompra * 0.3;
            return "La compra ha obtenido un 30% de descuento, por lo tanto su compra tiene el valor de: "
                    + resultadoDescuento + ", además obtuvo un regalo";
        } else if (valorDeCompra >= 160 && valorDeCompra <= 200) {
            resultadoDescuento = valorDeCompra - valorDeCompra * 0.2;
            return "La compra ha obtenido un 20% de descuento, por lo tanto su compra tiene el valor de: "
                    + resultadoDescuento;
        } else if (valorDeCompra == 150) {
            resultadoDescuento = valorDeCompra - valorDeCompra * 0.15;
            return "La compra ha obtenido un 15% de descuento, por lo tanto su compra tiene el valor de: "
                    + resultadoDescuento;
        } else if (valorDeCompra > 100) {
            resultadoDescuento = valorDeCompra - valorDeCompra * 0.1;
            return "La compra ha obtenido un 10% de descuento, por lo tanto su compra tiene el valor de: "
                    + resultadoDescuento;
        } else {
            return "La compra no ha obtenido ningún descuento, por lo tanto su compra tiene el valor de: "
                    + valorDeCompra;
        }
    }

    public static void main(String[] args) {
        System.out.println("Ingrese el valor de su compra: ");
        Double valorDeCompra = readScanner.nextDouble();
        String respValidacionDescuento = comprobarDescuento(valorDeCompra);
        System.out.println(respValidacionDescuento);
    }
}
