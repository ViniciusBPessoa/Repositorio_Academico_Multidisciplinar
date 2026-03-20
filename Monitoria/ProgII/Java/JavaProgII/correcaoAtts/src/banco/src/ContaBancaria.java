import java.util.ArrayList;

public class ContaBancaria {
    private int numeroConta;
    private String titular;
    private double saldo;
    private ArrayList<String> historicoTransacoes;

    public ContaBancaria(int numeroConta, String titular, double saldoInicial) {
        this.numeroConta = numeroConta;
        this.titular = titular;
        this.saldo = saldoInicial;
        this.historicoTransacoes = new ArrayList<>();
        salvarHistorico("Conta criada com saldo inicial de R$ " + saldoInicial);
    }

    public int getNumeroConta() { return numeroConta; }
    public String getTitular() { return titular; }
    public double getSaldo() { return saldo; }

    // Método protegido para permitir sobrescrita em subclasses
    protected void setSaldo(double saldo) { this.saldo = saldo; }

    public void creditarConta(double valor, String descricao) {
        if (valor > 0) {
            saldo += valor;
            salvarHistorico("Crédito: +" + valor + " | " + descricao);
            System.out.println("Depósito de R$ " + valor + " realizado na conta " + numeroConta);
        } else {
            System.out.println("Valor inválido para depósito.");
        }
    }

    public boolean debitarConta(double valor, String descricao) {
        if (valor > 0 && saldo >= valor) {
            saldo -= valor;
            salvarHistorico("Débito: -" + valor + " | " + descricao);
            System.out.println("Saque de R$ " + valor + " realizado na conta " + numeroConta);
            return true;
        } else {
            System.out.println("Saldo insuficiente ou valor inválido.");
            return false;
        }
    }

    public boolean transferirConta(ContaBancaria contaDestino, double valor, String descricao) {
        if (this.debitarConta(valor, "Transferência para conta " + contaDestino.getNumeroConta() + " | " + descricao)) {
            contaDestino.creditarConta(valor, "Transferência recebida da conta " + this.numeroConta);
            return true;
        }
        return false;
    }

    public void exibirExtrato() {
        System.out.println("\n=== Extrato da Conta " + numeroConta + " ===");
        for (String item : historicoTransacoes) {
            System.out.println(item);
        }
        System.out.println("Saldo atual: R$ " + saldo);
        System.out.println("-----------------------------");
    }

    private void salvarHistorico(String mensagem) {
        historicoTransacoes.add(mensagem);
    }
}