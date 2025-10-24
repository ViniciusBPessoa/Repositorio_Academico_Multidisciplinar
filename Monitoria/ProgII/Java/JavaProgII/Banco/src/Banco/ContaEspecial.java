package Banco;

public class ContaEspecial extends ContaBancaria {
    private double limite;
    private double taxaManutencao;

    public ContaEspecial(int numeroConta, String titular, double saldo, double limite) {
        super(numeroConta, titular, saldo);
        this.limite = limite;
        this.taxaManutencao = 10.0; // Taxa fixa de R$ 10,00
    }

    @Override
    public boolean debitarConta(double valor, String descricao) {
        if (valor <= 0) {
            System.out.println("Erro: Valor de débito deve ser positivo");
            return false;
        }
        
        double saldoAtual = getSaldo();
        if (saldoAtual + limite >= valor) {
            setSaldo(saldoAtual - valor);
            salvarHistorico("DÉBITO ESPECIAL: -R$ " + valor + " - " + descricao + " - Saldo: R$ " + getSaldo());
            return true;
        } else {
            salvarHistorico("TENTATIVA DE DÉBITO ESPECIAL FALHOU: -R$ " + valor + " - " + descricao + 
                           " - Saldo+limite insuficiente: R$ " + (saldoAtual + limite));
            return false;
        }
    }

    public void aplicarTaxaManutencao() {
        double saldoAtual = getSaldo();
        setSaldo(saldoAtual - taxaManutencao);
        salvarHistorico("TAXA DE MANUTENÇÃO: -R$ " + taxaManutencao + " - Saldo: R$ " + getSaldo());
    }

    // Getters
    public double getLimite() {
        return limite;
    }

    public double getTaxaManutencao() {
        return taxaManutencao;
    }
}