package Banco;


public class Main {
    public static void main(String[] args) {
        // Criar banco
        Banco banco = new Banco("Banco Java");
        
        // Criar contas
        banco.criaContaNormal(1001, "João Silva", 1000.0);
        banco.criaContaEspecial(1002, "Maria Santos", 500.0, 200.0);
        banco.criaContaPoupanca(1003, "Pedro Oliveira", 2000.0, 0.5);
        
        System.out.println("\n--- Operações Bancárias ---");
        
        // Operações de crédito
        banco.creditar(1001, 300.0, "Depósito em dinheiro");
        banco.creditar(1002, 200.0, "Transferência recebida");
        
        // Operações de débito
        banco.debitar(1001, 150.0, "Pagamento de conta");
        banco.debitar(1002, 800.0, "Saque especial"); // Usará o limite
        
        // Transferência
        banco.transferir(1001, 1003, 100.0, "Pagamento de serviço");
        
        System.out.println("\n--- Consultas ---");
        
        // Exibir saldos
        banco.exibirSaldo(1001);
        banco.exibirSaldo(1002);
        banco.exibirSaldo(1003);
        
        System.out.println("\n--- Extratos ---");
        banco.exibirExtrato(1001);
        banco.exibirExtrato(1003);
        
        System.out.println("\n--- Lista de Contas ---");
        banco.listarContas();
        
        System.out.println("\n--- Operações Especiais ---");
        
        // Aplicar rendimento na poupança
        ContaPoupanca poupanca = (ContaPoupanca) banco.getContasCadastradas().get(2);
        poupanca.aplicarRendimento();
        banco.exibirSaldo(1003);
        
        // Aplicar taxa de manutenção na conta especial
        ContaEspecial especial = (ContaEspecial) banco.getContasCadastradas().get(1);
        especial.aplicarTaxaManutencao();
        banco.exibirSaldo(1002);
    }
}