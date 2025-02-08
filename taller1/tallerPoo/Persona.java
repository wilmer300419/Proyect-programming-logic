public class Persona {

    private Long codIdentificacion;
    private String nombre;
    private String apellido;


    public Persona(Long codIdentificacion, String nombre, String apellido) {
        this.codIdentificacion = codIdentificacion;
        this.nombre = nombre;
        this.apellido = apellido;
    }

    public Persona(){}


    public Long getCodIdentificacion() {
        return codIdentificacion;
    }


    public void setCodIdentificacion(Long codIdentificacion) {
        this.codIdentificacion = codIdentificacion;
    }


    public String getNombre() {
        return nombre;
    }


    public void setNombre(String nombre) {
        this.nombre = nombre;
    }


    public String getApellido() {
        return apellido;
    }


    public void setApellido(String apellido) {
        this.apellido = apellido;
    }

    

    
    
}
