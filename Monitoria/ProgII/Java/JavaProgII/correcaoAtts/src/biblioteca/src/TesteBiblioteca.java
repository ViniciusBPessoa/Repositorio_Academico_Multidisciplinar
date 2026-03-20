public class TesteBiblioteca {
    public static void main(String[] args) {
        Biblioteca biblioteca = new Biblioteca("Biblioteca Central");

        Livro l1 = new Livro("O Pequeno Príncipe", "Antoine de Saint-Exupéry", 1943);
        Livro l2 = new Livro("Dom Casmurro", "Machado de Assis", 1899);
        Revista r1 = new Revista("Revista Ciência Hoje", "Redação", 2025, 125, "Outubro");

        biblioteca.cadastrarLivro(l1);
        biblioteca.cadastrarLivro(l2);
        biblioteca.cadastrarRevista(r1);

        System.out.println();
        biblioteca.listarAcervo();

        System.out.println();
        biblioteca.emprestarItem("Dom Casmurro");
        biblioteca.emprestarItem("Revista Ciência Hoje");

        System.out.println();
        biblioteca.listarAcervo();

        System.out.println();
        biblioteca.devolverItem("Dom Casmurro");
        biblioteca.listarAcervo();
    }
}
