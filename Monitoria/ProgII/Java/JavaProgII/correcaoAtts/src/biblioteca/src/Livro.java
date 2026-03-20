public class Livro {
    private String titulo;
    private String autor;
    private int ano;
    private boolean emprestado;


    public Livro(String titulo, String autor, int ano) {
        this.titulo = titulo;
        this.autor = autor;
        this.ano = ano;
        this.emprestado = false;
    }

    public String getTitulo() {
        return titulo;
    }
    public String  getAutor() {
        return autor;
    }
    public int getAno() {
        return ano;
    }

    public boolean isEmprestado() {
        return emprestado;
    }

    public void emprestar() {
        if (!emprestado) {
            emprestado = true;
            System.out.println("Livro" + titulo + " emprestado");
        } else {
            System.out.println("Livro" + titulo + " já emprestado");
        }
    }


    public void devolver() {
        if (emprestado) {
            emprestado = false;
            System.out.println("Livro" + titulo + " devolvido");
        } else {
            System.out.println(" Livro " + titulo + "não estava emprestado");
        }
    }

    public void exibirInfo() {
        System.out.println("=== Livro ===");
        System.out.println("Título: " + titulo);
        System.out.println("Autor: " + autor);
        System.out.println("Ano: " + ano);
        System.out.println("Status: " + (emprestado ? "Emprestado" : "Disponível"));
        System.out.println("---------------------------");
    }
}
