public class Revista extends Livro{
    private int numeroEdicao;
    private String mes;

    public int getNumeroEdicao() {
        return numeroEdicao;
    }
    public String getMes() {
        return mes;
    }

    public Revista(String titulo, String autor, int ano, int numeroEdicao, String mes) {
        super(titulo, autor, ano);
        this.numeroEdicao = numeroEdicao;
        this.mes = mes;
    }

    @Override
    public void exibirInfo(){
        System.out.println("=== Revista ===");
        System.out.println("Título: " + getTitulo());
        System.out.println("Autor: " + getAutor());
        System.out.println("Ano: " + getAno());
        System.out.println("Edição: " + numeroEdicao);
        System.out.println("Mês: " + mes);
        System.out.println("Status: " + (isEmprestado() ? "Emprestado" : "Disponível"));
        System.out.println("---------------------------");
    }
}
