package Banco;

import java.util.ArrayList;

public class Banco {
    
    private String nomeBanco;
    private ArrayList<ContaBancaria> contasCadastradas;
    
    public Banco(String nomeBanco) {
        this.nomeBanco = nomeBanco;
        this.contasCadastradas = new ArrayList<ContaBancaria>();
    }
    
    public void criaConta(int numeroConta, String titular, double saldoInicial) {
        for (ContaBancaria contaBancaria : contasCadastradas) {
            if (contaBancaria.getNumeroConta() == numeroConta) {
                System.out.println("Conta número " + numeroConta + " já existente");
                return;
            }
        }
        
        ContaBancaria contaAtual = new ContaBancaria(numeroConta, titular, saldoInicial);
        contasCadastradas.add(contaAtual);
        System.out.println("Conta número " + numeroConta + " criada com sucesso");
    }
    
    public boolean debitar(int numeroConta, double valor, String descricao) {
        ContaBancaria conta = buscarConta(numeroConta);
        if (conta != null) {
            boolean sucesso = conta.debitarConta(valor, descricao);
            if (sucesso) {
                System.out.println("Débito de R$ " + valor + " realizado na conta " + numeroConta);
            } else {
                System.out.println("Falha no débito na conta " + numeroConta);
            }
            return sucesso;
        } else {
            System.out.println("Conta " + numeroConta + " não encontrada");
            return false;
        }
    }
    
    public void creditar(int numeroConta, double valor, String descricao) {
        ContaBancaria conta = buscarConta(numeroConta);
        if (conta != null) {
            conta.creditarConta(valor, descricao);
            System.out.println("Crédito de R$ " + valor + " realizado na conta " + numeroConta);
        } else {
            System.out.println("Conta " + numeroConta + " não encontrada");
        }
    }
    
    public boolean transferir(int numeroContaOrigem, int numeroContaDestino, double valor, String descricao) {
        ContaBancaria contaOrigem = buscarConta(numeroContaOrigem);
        ContaBancaria contaDestino = buscarConta(numeroContaDestino);
        
        if (contaOrigem == null) {
            System.out.println("Conta origem " + numeroContaOrigem + " não encontrada");
            return false;
        }
        
        if (contaDestino == null) {
            System.out.println("Conta destino " + numeroContaDestino + " não encontrada");
            return false;
        }
        
        if (contaOrigem.transferir(contaDestino, valor, descricao)) {
            System.out.println("Transferência de R$ " + valor + " realizada de " + 
                             numeroContaOrigem + " para " + numeroContaDestino);
            return true;
        } else {
            System.out.println("Falha na transferência da conta " + numeroContaOrigem);
            return false;
        }
    }
    
    public void exibirSaldo(int numeroConta) {
        ContaBancaria conta = buscarConta(numeroConta);
        if (conta != null) {
            System.out.println("Saldo da conta " + numeroConta + ": R$ " + conta.getSaldo());
        } else {
            System.out.println("Conta " + numeroConta + " não encontrada");
        }
    }
    
    public void exibirExtrato(int numeroConta) {
        ContaBancaria conta = buscarConta(numeroConta);
        if (conta != null) {
            conta.exibirExtrato();
        } else {
            System.out.println("Conta " + numeroConta + " não encontrada");
        }
    }
    
    private ContaBancaria buscarConta(int numeroConta) {
        for (ContaBancaria conta : contasCadastradas) {
            if (conta.getNumeroConta() == numeroConta) {
                return conta;
            }
        }
        return null;
    }
    
    public void listarContas() {
        System.out.println("\n=== Contas Cadastradas no " + nomeBanco + " ===");
        if (contasCadastradas.isEmpty()) {
            System.out.println("Nenhuma conta cadastrada");
        } else {
            for (ContaBancaria conta : contasCadastradas) {
                System.out.println("Conta: " + conta.getNumeroConta() + 
                                 " - Titular: " + conta.getTitular() + 
                                 " - Saldo: R$ " + conta.getSaldo());
            }
        }
    }

    // Getters e Setters
    public String getNomeBanco() {
        return nomeBanco;
    }

    public void setNomeBanco(String nomeBanco) {
        this.nomeBanco = nomeBanco;
    }

    public ArrayList<ContaBancaria> getContasCadastradas() {
        return new ArrayList<>(contasCadastradas); // Retorna cópia para evitar modificação externa
    }

    public void setContasCadastradas(ArrayList<ContaBancaria> contasCadastradas) {
        this.contasCadastradas = contasCadastradas;
    }
}