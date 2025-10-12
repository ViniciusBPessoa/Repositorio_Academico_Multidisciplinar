package Banco;

public class Main {

	public static void main(String[] args) {
        Banco banco = new Banco("Banco Digital");
        
        // Criar contas
        banco.criaConta(101, "João Silva", 1000.0);
        banco.criaConta(102, "Maria Santos", 500.0);
        
        // Operações
        banco.creditar(101, 200.0, "Depósito");
        banco.debitar(101, 150.0, "Saque");
        banco.transferir(101, 102, 100.0, "Pagamento");
        
        // Consultas
        banco.exibirSaldo(101);
        banco.exibirExtrato(102);
        banco.listarContas();   
	}
}
