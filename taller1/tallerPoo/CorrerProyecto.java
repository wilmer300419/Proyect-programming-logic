
import java.util.Scanner;

public class CorrerProyecto{

    public static void main(String[] args) {

        PromedioNotasEstudiante promedioNotasEstudiante1 = new PromedioNotasEstudiante();
        int resp = 1;
        Scanner readScanner = new Scanner(System.in);
        
        Long codID;

        String nombre;
        String apellido;
        String materia;
        String curso;

        while(resp==1){
            System.out.println("El programa se centrara en promediar las notas de los estudiantes que se ingrese");

            System.out.println("Ingrese el codigo del estudiante: ");
            codID = readScanner.nextLong();

            System.out.println("Ingrese el(los) nombre(s) del(la) estudiante: ");
            readScanner.nextLine();
            nombre = readScanner.nextLine();

            System.out.println("Ingrese los apellidos: ");
            apellido = readScanner.nextLine();

            System.out.println("Ingrese el curso del estudiante: ");
            curso = readScanner.nextLine();

            System.out.println("Ingrese la materia a la cual se le van a promediar las notas: ");
            materia = readScanner.nextLine();

            promedioNotasEstudiante1.promediarNotas(codID, nombre, apellido, materia, curso);

            System.out.println("¿Desea seguir usando nuestro programa? escriba el codigo de una de las opciones:");
            System.out.println("1. Si \2. No");

            resp = readScanner.nextInt();

            if(resp !=1 || resp !=2) System.out.println("El programa se cerro porque se ingreso un valor erroneo.");

        }

        System.out.println("Gracias por usar nuestro programa");
        
    }
}