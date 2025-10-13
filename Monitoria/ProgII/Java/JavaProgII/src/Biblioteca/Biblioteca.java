package Biblioteca;

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
        System.out.println("Livro '" + livro.getTitulo() + "' cadastrado com sucesso!");
    }
    
    public void cadastrarRevista(Revista revista) {
        acervo.add(revista);
        System.out.println("Revista '" + revista.getTitulo() + "' cadastrada com sucesso!");
    }
    
    public boolean emprestarItem(String titulo) {
        for (Livro item : acervo) {
            if (item.getTitulo().equals(titulo)) {
                if (!item.isEmprestado()) {
                    item.emprestar();
                    return true;
                } else {
                    System.out.println("Item '" + titulo + "' já está emprestado!");
                    return false;
                }
            }
        }
        System.out.println("Item '" + titulo + "' não encontrado no acervo!");
        return false;
    }
    
    public boolean devolverItem(String titulo) {
        for (Livro item : acervo) {
            if (item.getTitulo().equals(titulo)) {
                item.devolver();
                return true;
            }
        }
        System.out.println("Item '" + titulo + "' não encontrado no acervo!");
        return false;
    }
    
    public void listarAcervo() {
        System.out.println("\n=== ACERVO DA " + nome.toUpperCase() + " ===");
        if (acervo.isEmpty()) {
            System.out.println("Acervo vazio!");
        } else {
            for (Livro item : acervo) {
                item.exibirInfo();
            }
        }
    }
    
    public void listarDisponiveis() {
        System.out.println("\n=== ITENS DISPONÍVEIS ===");
        boolean encontrou = false;
        for (Livro item : acervo) {
            if (!item.isEmprestado()) {
                item.exibirInfo();
                encontrou = true;
            }
        }
        if (!encontrou) {
            System.out.println("Nenhum item disponível no momento!");
        }
    }

	public String getNome() {
		return nome;
	}

	public void setNome(String nome) {
		this.nome = nome;
	}

	public ArrayList<Livro> getAcervo() {
		return acervo;
	}

	public void setAcervo(ArrayList<Livro> acervo) {
		this.acervo = acervo;
	}
    
    
    
}
