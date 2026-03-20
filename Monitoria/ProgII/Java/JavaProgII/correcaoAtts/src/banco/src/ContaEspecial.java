public class ContaEspecial extends ContaBancaria {
    private double limite;
    private double taxaManutencao;

    public ContaEspecial(int numeroConta, String titular, double saldoInicial, double limite) {
        super(numeroConta, titular, saldoInicial);
        this.limite = limite;
        this.taxaManutencao = 25.0; // exemplo
    }

    public double getLimite() { return limite; }
    public double getTaxaManutencao() { return taxaManutencao; }

    @Override
    public boolean debitarConta(double valor, String descricao) {
        double saldoDisponivel = getSaldo() + limite;
        if (valor > 0 && saldoDisponivel >= valor) {
            setSaldo(getSaldo() - valor);
            System.out.println("Saque de R$ " + valor + " realizado na conta especial " + getNumeroConta());
            return true;
        } else {
            System.out.println("Saldo + limite insuficiente.");
            return false;
        }
    }

    public void aplicarTaxaManutencao() {
        debitarConta(taxaManutencao, "Taxa de manutenção");
    }
}
