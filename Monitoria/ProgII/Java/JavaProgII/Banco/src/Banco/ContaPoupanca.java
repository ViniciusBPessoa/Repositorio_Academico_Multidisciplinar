package Banco;

public class ContaPoupanca extends ContaBancaria {
    private double taxaRendimento;

    public ContaPoupanca(int numeroConta, String titular, double saldo, double taxaRendimento) {
        super(numeroConta, titular, saldo);
        this.taxaRendimento = taxaRendimento;
    }

    public void aplicarRendimento() {
        double rendimento = getSaldo() * (taxaRendimento / 100);
        setSaldo(getSaldo() + rendimento);
        salvarHistorico("RENDIMENTO: +R$ " + rendimento + " (" + taxaRendimento + "%) - Saldo: R$ " + getSaldo());
    }

    // Getter
    public double getTaxaRendimento() {
        return taxaRendimento;
    }
}