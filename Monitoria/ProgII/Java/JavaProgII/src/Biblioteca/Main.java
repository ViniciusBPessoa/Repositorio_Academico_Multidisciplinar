package Biblioteca;

public class Main {
    public static void main(String[] args) {
        // Criar biblioteca
        Biblioteca biblioteca = new Biblioteca("Biblioteca Municipal");
        
        // Criar livros e revistas
        Livro livro1 = new Livro("Dom Casmurro", "Machado de Assis", 1899);
        Livro livro2 = new Livro("O Cortiço", "Aluísio Azevedo", 1890);
        Revista revista1 = new Revista("Veja", "Editora Abril", 2024, 2876, "Março");
        Revista revista2 = new Revista("Época", "Editora Globo", 2024, 952, "Abril");
        
        // Cadastrar no acervo
        biblioteca.cadastrarLivro(livro1);
        biblioteca.cadastrarLivro(livro2);
        biblioteca.cadastrarRevista(revista1);
        biblioteca.cadastrarRevista(revista2);
        
        // Operações
        System.out.println("\n--- OPERAÇÕES ---");
        biblioteca.emprestarItem("Dom Casmurro");
        biblioteca.emprestarItem("Veja");
        biblioteca.emprestarItem("Livro Inexistente"); // Teste erro
        
        // Listagens
        biblioteca.listarAcervo();
        biblioteca.listarDisponiveis();
        
        // Devoluções
        System.out.println("\n--- DEVOLUÇÕES ---");
        biblioteca.devolverItem("Dom Casmurro");
        biblioteca.listarDisponiveis();
    }
}
