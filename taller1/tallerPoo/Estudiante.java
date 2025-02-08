

public class Estudiante extends Persona {

    private String cursoEstudiante;
    private String materiaEstudiante;

    public Estudiante(Long codIdentificacion, String nombre, String apellido, String materiaEstudiante, String cursoEstudiante) {
        super(codIdentificacion, nombre, apellido);
        this.cursoEstudiante = cursoEstudiante;
        this.materiaEstudiante = materiaEstudiante;
    }

    public String getCursoEstudiante() {
        return cursoEstudiante;
    }

    public void setCursoEstudiante(String cursoEstudiante) {
        this.cursoEstudiante = cursoEstudiante;
    }

    public String getMateriaEstudiante() {
        return materiaEstudiante;
    }

    public void setMateriaEstudiante(String materiaEstudiante) {
        this.materiaEstudiante = materiaEstudiante;
    }


    
    
}
