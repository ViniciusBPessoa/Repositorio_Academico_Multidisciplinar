import java.util.ArrayList;

public class Biblioteca {
    private String nome;
    private ArrayList<Livro> acervo;

    public Biblioteca(String nome) {
        this.nome = nome;
        this.acervo = new ArrayList<>();
    }

    public void cadastrarLivro(Livro livro) {
        acervo.add(livro);
        System.out.println("Livro \"" + livro.getTitulo() + "\" cadastrado no acervo.");
    }

    public void cadastrarRevista(Revista revista) {
        acervo.add(revista);
        System.out.println("Revista \"" + revista.getTitulo() + "\" cadastrada no acervo.");
    }

    public boolean emprestarItem(String titulo) {
        for (Livro item : acervo) {
            if (item.getTitulo().equalsIgnoreCase(titulo)) {
                if (!item.isEmprestado()) {
                    item.emprestar();
                    return true;
                } else {
                    System.out.println("Item \"" + titulo + "\" já está emprestado.");
                    return false;
                }
            }
        }
        System.out.println("Item \"" + titulo + "\" não encontrado no acervo.");
        return false;
    }

    public boolean devolverItem(String titulo) {
        for (Livro item : acervo) {
            if (item.getTitulo().equalsIgnoreCase(titulo)) {
                if (item.isEmprestado()) {
                    item.devolver();
                    return true;
                } else {
                    System.out.println("Item \"" + titulo + "\" já estava disponível.");
                    return false;
                }
            }
        }
        System.out.println("Item \"" + titulo + "\" não encontrado no acervo.");
        return false;
    }

    public void listarAcervo() {
        System.out.println("=== Acervo da Biblioteca " + nome + " ===");
        for (Livro item : acervo) {
            item.exibirInfo();
        }
    }
}