package Banco;

import java.util.ArrayList;

public class ContaBancaria {
    private int numeroConta;
    private String titular;
    private double saldo;
    private ArrayList<String> historicoTransacoes;

    public ContaBancaria(int numeroConta, String titular, double saldo) {
        this.numeroConta = numeroConta;
        this.titular = titular;
        this.saldo = saldo;
        this.historicoTransacoes = new ArrayList<>();
        salvarHistorico("Conta criada com saldo inicial: R$ " + saldo);
    }

    public void creditarConta(double valor, String descricao) {
        if (valor <= 0) {
            System.out.println("Erro: Valor de crédito deve ser positivo");
        }
        
        saldo += valor;
        salvarHistorico("CRÉDITO: +R$ " + valor + " - " + descricao + " - Saldo: R$ " + saldo);
    }

    public boolean debitarConta(double valor, String descricao) {
        if (valor <= 0) {
            System.out.println("Erro: Valor de débito deve ser positivo");
            return false;
        }
        
        if (saldo >= valor) {
            saldo -= valor;
            salvarHistorico("DÉBITO: -R$ " + valor + " - " + descricao + " - Saldo: R$ " + saldo);
            return true;
        } else {
            salvarHistorico("TENTATIVA DE DÉBITO FALHOU: -R$ " + valor + " - " + descricao + " - Saldo insuficiente: R$ " + saldo);
            return false;
        }
    }

    public boolean transferirConta(ContaBancaria contaDestino, double valor, String descricao) {
        if (debitarConta(valor, "Transferência para conta " + contaDestino.getNumeroConta() + ": " + descricao)) {
            contaDestino.creditarConta(valor, "Transferência da conta " + numeroConta + ": " + descricao);
            return true;
        }
        return false;
    }

    public void exibirExtrato() {
        if (historicoTransacoes.isEmpty()) {
            System.out.println("Nenhuma transação realizada");
            return;
        }
        
        for (String transacao : historicoTransacoes) {
            System.out.println(transacao);
        }
        System.out.println("Saldo atual: R$ " + saldo);
    }

    public void salvarHistorico(String mensagem) {
        historicoTransacoes.add(mensagem);
    }

    // Getters
    public int getNumeroConta() {
        return numeroConta;
    }

    public String getTitular() {
        return titular;
    }

    public double getSaldo() {
        return saldo;
    }

    public ArrayList<String> getHistoricoTransacoes() {
        return historicoTransacoes;
    }

    // Setter protegido para saldo (usado pelas classes filhas)
    protected void setSaldo(double saldo) {
        this.saldo = saldo;
    }
}