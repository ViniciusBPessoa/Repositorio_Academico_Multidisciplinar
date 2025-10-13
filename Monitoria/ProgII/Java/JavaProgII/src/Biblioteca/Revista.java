package Biblioteca;

public class Revista extends Livro {
    private int numeroEdicao;
    private String mes;
    
    public Revista(String titulo, String autor, int ano, int numeroEdicao, String mes) {
        super(titulo, autor, ano);
        this.numeroEdicao = numeroEdicao;
        this.mes = mes;
    }
    
    @Override
    public void exibirInfo() {
        String status = emprestado ? "Emprestado" : "Disponível";
        System.out.println("Revista: " + titulo + " | Editora: " + autor + " | Edição: " + numeroEdicao + 
                          " | Mês: " + mes + " | Ano: " + ano + " | Status: " + status);
    }

	public int getNumeroEdicao() {
		return numeroEdicao;
	}

	public void setNumeroEdicao(int numeroEdicao) {
		this.numeroEdicao = numeroEdicao;
	}

	public String getMes() {
		return mes;
	}

	public void setMes(String mes) {
		this.mes = mes;
	}
    
}