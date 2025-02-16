
import java.util.Scanner;

public class PromedioNotasEstudiante {

    private float nota;
    private float acumuladorNotaEstudiante;
    private float promedioNotaEstudiante;
    
    public PromedioNotasEstudiante(float nota, float acumuladorNotaEstudiante, float promedioNotaEstudiante) {
        this.nota = nota;
        this.acumuladorNotaEstudiante = acumuladorNotaEstudiante;
        this.promedioNotaEstudiante = promedioNotaEstudiante;
    }

    public PromedioNotasEstudiante(){}

    public float getNota() {
        return nota;
    }

    public void setNota(float nota) {
        this.nota = nota;
    }

    public float getAcumuladorNotaEstudiante() {
        return acumuladorNotaEstudiante;
    }

    public void setAcumuladorNotaEstudiante(float acumuladorNotaEstudiante) {
        this.acumuladorNotaEstudiante = acumuladorNotaEstudiante;
    }

    public float getPromedioNotaEstudiante() {
        return promedioNotaEstudiante;
    }

    public void setPromedioNotaEstudiante(float promedioNotaEstudiante) {
        this.promedioNotaEstudiante = promedioNotaEstudiante;
    }

    public void promediarNotas(Long codIdentificacion, String nombre, String apellido, String materiaEstudiante, String cursoEstudiante){
            
        Scanner readScanner = new Scanner(System.in);

        Estudiante estudiante  = new Estudiante(codIdentificacion, nombre, apellido, materiaEstudiante, cursoEstudiante);

        String nombreEst = estudiante.getNombre();
        String apellidoEst = estudiante.getApellido();
        String materiaEst = estudiante.getMateriaEstudiante();
        String cursoEst = estudiante.getCursoEstudiante();
        Long codEst = estudiante.getCodIdentificacion();

        System.out.println("De acuerdo a los datos suministrados se le van a promediar las notas de " + materiaEst + " a el estudiante: " + codEst+ ". " + nombreEst + " " + apellidoEst+" del curso: "+ cursoEst+".");
        System.out.println("Ingrese la cantidad de notas que desea promediar: ");
        int nNotas = readScanner.nextInt();
        
        for (int i = 0; i < nNotas; i++) {
            System.out.println("Ingrese la nota #"+(i+1));
            this.setNota(readScanner.nextFloat());
            this.setAcumuladorNotaEstudiante(this.getAcumuladorNotaEstudiante()+this.nota);
        }
        
        this.setPromedioNotaEstudiante(this.getAcumuladorNotaEstudiante()/nNotas);
        System.out.println("El promedio de las notas de "+ materiaEst + " del estudiante " + nombreEst + " " + apellidoEst+" es: "+ this.getPromedioNotaEstudiante()+".");

    }

    
    


}
