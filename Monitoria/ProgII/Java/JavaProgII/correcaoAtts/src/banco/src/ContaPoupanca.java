public class ContaPoupanca extends ContaBancaria {
    private double taxaRendimento;

    public ContaPoupanca(int numeroConta, String titular, double saldoInicial, double taxaRendimento) {
        super(numeroConta, titular, saldoInicial);
        this.taxaRendimento = taxaRendimento;
    }

    public void aplicarRendimento() {
        double rendimento = getSaldo() * taxaRendimento; // 0.02 = 2%
        creditarConta(rendimento, "Rendimento mensal aplicado");
        System.out.println("Rendimento de R$ " + rendimento + " aplicado na conta " + getNumeroConta());
    }
}