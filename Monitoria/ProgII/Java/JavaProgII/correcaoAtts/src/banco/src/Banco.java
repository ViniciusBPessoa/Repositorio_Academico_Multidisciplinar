import java.util.ArrayList;

public class Banco {
    private String nomeBanco;
    private ArrayList<ContaBancaria> contasCadastradas;

    public Banco(String nomeBanco) {
        this.nomeBanco = nomeBanco;
        contasCadastradas = new ArrayList<>();
    }

    private ContaBancaria buscarConta(int numeroConta) {
        for (ContaBancaria c : contasCadastradas) {
            if (c.getNumeroConta() == numeroConta) return c;
        }
        return null;
    }

    public boolean criaContaNormal(int numeroConta, String titular, double saldoInicial) {
        if (buscarConta(numeroConta) != null) return false;
        contasCadastradas.add(new ContaBancaria(numeroConta, titular, saldoInicial));
        return true;
    }

    public boolean criaContaEspecial(int numeroConta, String titular, double saldoInicial, double limite) {
        if (buscarConta(numeroConta) != null) return false;
        contasCadastradas.add(new ContaEspecial(numeroConta, titular, saldoInicial, limite));
        return true;
    }

    public boolean criaContaPoupanca(int numeroConta, String titular, double saldoInicial, double taxaRendimento) {
        if (buscarConta(numeroConta) != null) return false;
        contasCadastradas.add(new ContaPoupanca(numeroConta, titular, saldoInicial, taxaRendimento));
        return true;
    }

    public boolean debitar(int numeroConta, double valor, String descricao) {
        ContaBancaria c = buscarConta(numeroConta);
        return (c != null) && c.debitarConta(valor, descricao);
    }

    public void creditar(int numeroConta, double valor, String descricao) {
        ContaBancaria c = buscarConta(numeroConta);
        if (c != null) c.creditarConta(valor, descricao);
    }

    public boolean transferir(int origem, int destino, double valor, String descricao) {
        ContaBancaria cOrigem = buscarConta(origem);
        ContaBancaria cDestino = buscarConta(destino);
        return (cOrigem != null && cDestino != null) && cOrigem.transferirConta(cDestino, valor, descricao);
    }

    public void exibirSaldo(int numeroConta) {
        ContaBancaria c = buscarConta(numeroConta);
        if (c != null) System.out.println("Saldo da conta " + numeroConta + ": R$ " + c.getSaldo());
        else System.out.println("Conta não encontrada.");
    }

    public void exibirExtrato(int numeroConta) {
        ContaBancaria c = buscarConta(numeroConta);
        if (c != null) c.exibirExtrato();
    }

    public void listarContas() {
        System.out.println("\n=== Contas cadastradas no banco " + nomeBanco + " ===");
        for (ContaBancaria c : contasCadastradas) {
            System.out.println("Conta " + c.getNumeroConta() + " | Titular: " + c.getTitular() + " | Saldo: R$ " + c.getSaldo());
        }
    }
}