package Biblioteca;

public class Livro {
    protected String titulo;
    protected String autor;
    protected int ano;
    protected String Editora;
    protected boolean emprestado;
    
    public Livro(String titulo, String autor, int ano) {
        this.titulo = titulo;
        this.autor = autor;
        this.ano = ano;
        this.emprestado = false;
        this.Editora = "lIVRO";
    }
    public Livro(String titulo, String autor, int ano, String Editora) {
        this.titulo = titulo;
        this.autor = autor;
        this.ano = ano;
        this.emprestado = false;
        this.Editora = Editora;
    }
    
    public void emprestar() {
        if (!emprestado) {
            emprestado = true;
            System.out.println("Livro '" + titulo + "' emprestado com sucesso!");
        } else {
            System.out.println("Livro '" + titulo + "' já está emprestado!");
        }
    }
    
    public void devolver() {
        if (emprestado) {
            emprestado = false;
            System.out.println("Livro '" + titulo + "' devolvido com sucesso!");
        } else {
            System.out.println("Livro '" + titulo + "' não estava emprestado!");
        }
    }
    
    public void exibirInfo() {
        String status = emprestado ? "Emprestado" : "Disponível";
        System.out.println("Livro: " + titulo + " | Autor: " + autor + " | Ano: " + ano + " | Status: " + status);
    }

	public String getTitulo() {
		return titulo;
	}

	public void setTitulo(String titulo) {
		this.titulo = titulo;
	}

	public String getAutor() {
		return autor;
	}

	public void setAutor(String autor) {
		this.autor = autor;
	}

	public int getAno() {
		return ano;
	}

	public void setAno(int ano) {
		this.ano = ano;
	}

	public boolean isEmprestado() {
		return emprestado;
	}

	public void setEmprestado(boolean emprestado) {
		this.emprestado = emprestado;
	}
    
    
}