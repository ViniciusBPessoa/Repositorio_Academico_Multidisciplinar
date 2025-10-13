package Banco;

import java.util.ArrayList;

public class ContaBancaria {
    
    private int numeroConta;
    private String titular;
    private Double saldo;
    private ArrayList<String> historicoTransacoes;
    
    public ContaBancaria(int numeroConta, String titular, double saldoInicial) {
        this.numeroConta = numeroConta;
        this.titular = titular;
        this.saldo = saldoInicial;
        this.historicoTransacoes = new ArrayList<>();
        this.historicoTransacoes.add("Conta criada com saldo inicial: R$ " + saldoInicial);
    }
    
    public void creditarConta(double valor, String descricao) {
        if (valor <= 0) {
            System.out.println("Valor de crédito deve ser positivo");
            return;
        }
        this.saldo += valor;
        salvarHistorico("Crédito: +R$ " + valor + " - " + descricao + " - Saldo: R$ " + this.saldo);
    }
    
    public boolean debitarConta(double valor, String descricao) {
        if (valor <= 0) {
            System.out.println("Valor de débito deve ser positivo");
            return false;
        }
        if (this.saldo - valor < 0) {
            System.out.println("Saldo insuficiente");
            return false;
        } else {
            this.saldo -= valor;
            salvarHistorico("Débito: -R$ " + valor + " - " + descricao + " - Saldo: R$ " + this.saldo);
            return true;
        }
    }
    
    public boolean transferirConta(ContaBancaria contaDestino, double valor, String descricao) {
        if (this.debitarConta(valor, "Transferência para " + contaDestino.getTitular() + ": " + descricao)) {
            contaDestino.creditarConta(valor, "Transferência de " + this.titular + ": " + descricao);
            return true;
        }
        return false;
    }
    
    private void salvarHistorico(String mensagem) {
        historicoTransacoes.add(java.time.LocalDateTime.now() + " - " + mensagem);
    }
    
    public void exibirExtrato() {
        System.out.println("\n=== Extrato da Conta " + numeroConta + " ===");
        System.out.println("Titular: " + titular);
        System.out.println("Saldo atual: R$ " + saldo);
        System.out.println("\nHistórico de transações:");
        for (String transacao : historicoTransacoes) {
            System.out.println(transacao);
        }
    }

    // Getters e Setters
    public int getNumeroConta() {
        return numeroConta;
    }

    public void setNumeroConta(int numeroConta) {
        this.numeroConta = numeroConta;
    }

    public String getTitular() {
        return titular;
    }

    public void setTitular(String titular) {
        this.titular = titular;
    }

    public Double getSaldo() {
        return saldo;
    }

    public void setSaldo(Double saldo) {
        this.saldo = saldo;
    }

    public ArrayList<String> getHistoricoTransacoes() {
        return new ArrayList<>(historicoTransacoes); // Retorna cópia para evitar modificação externa
    }

    public void setHistoricoTransacoes(ArrayList<String> historicoTransacoes) {
        this.historicoTransacoes = historicoTransacoes;
    }
}