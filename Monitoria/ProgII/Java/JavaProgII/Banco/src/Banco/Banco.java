package Banco;

import java.util.ArrayList;

public class Banco {
    private String nomeBanco;
    private ArrayList<ContaBancaria> contasCadastradas;
    private int proximoNumeroConta;

    public Banco(String nomeBanco) {
        this.nomeBanco = nomeBanco;
        this.contasCadastradas = new ArrayList<>();
        this.proximoNumeroConta = 1001; // Começa com 1001 como primeira conta
    }

    // Métodos sem número de conta como parâmetro (geração automática)
    public boolean criaContaNormal(String titular, double saldoInicial) {
        int numeroConta = gerarNumeroConta();
        ContaBancaria novaConta = new ContaBancaria(numeroConta, titular, saldoInicial);
        contasCadastradas.add(novaConta);
        System.out.println("Conta normal criada com sucesso para " + titular + " - Número: " + numeroConta);
        return true;
    }

    public boolean criaContaEspecial(String titular, double saldoInicial, double limite) {
        int numeroConta = gerarNumeroConta();
        ContaEspecial novaConta = new ContaEspecial(numeroConta, titular, saldoInicial, limite);
        contasCadastradas.add(novaConta);
        System.out.println("Conta especial criada com sucesso para " + titular + " - Número: " + numeroConta);
        return true;
    }

    public boolean criaContaPoupanca(String titular, double saldoInicial, double taxaRendimento) {
        int numeroConta = gerarNumeroConta();
        ContaPoupanca novaConta = new ContaPoupanca(numeroConta, titular, saldoInicial, taxaRendimento);
        contasCadastradas.add(novaConta);
        System.out.println("Conta poupança criada com sucesso para " + titular + " - Número: " + numeroConta);
        return true;
    }

    // Método privado para gerar número de conta automático
    private int gerarNumeroConta() {
        int numeroAtual = proximoNumeroConta;
        proximoNumeroConta++; // Incrementa para a próxima conta
        return numeroAtual;
    }

    // Mantemos os métodos originais que recebem número de conta (para compatibilidade)
    public boolean criaContaNormal(int numeroConta, String titular, double saldoInicial) {
        if (buscarConta(numeroConta) != null) {
            System.out.println("Erro: Já existe uma conta com o número " + numeroConta);
            return false;
        }
        
        // Atualiza o próximo número se necessário
        if (numeroConta >= proximoNumeroConta) {
            proximoNumeroConta = numeroConta + 1;
        }
        
        ContaBancaria novaConta = new ContaBancaria(numeroConta, titular, saldoInicial);
        contasCadastradas.add(novaConta);
        System.out.println("Conta normal criada com sucesso para " + titular);
        return true;
    }

    public boolean criaContaEspecial(int numeroConta, String titular, double saldoInicial, double limite) {
        if (buscarConta(numeroConta) != null) {
            System.out.println("Erro: Já existe uma conta com o número " + numeroConta);
            return false;
        }
        
        // Atualiza o próximo número se necessário
        if (numeroConta >= proximoNumeroConta) {
            proximoNumeroConta = numeroConta + 1;
        }
        
        ContaEspecial novaConta = new ContaEspecial(numeroConta, titular, saldoInicial, limite);
        contasCadastradas.add(novaConta);
        System.out.println("Conta especial criada com sucesso para " + titular);
        return true;
    }

    public boolean criaContaPoupanca(int numeroConta, String titular, double saldoInicial, double taxaRendimento) {
        if (buscarConta(numeroConta) != null) {
            System.out.println("Erro: Já existe uma conta com o número " + numeroConta);
            return false;
        }
        
        // Atualiza o próximo número se necessário
        if (numeroConta >= proximoNumeroConta) {
            proximoNumeroConta = numeroConta + 1;
        }
        
        ContaPoupanca novaConta = new ContaPoupanca(numeroConta, titular, saldoInicial, taxaRendimento);
        contasCadastradas.add(novaConta);
        System.out.println("Conta poupança criada com sucesso para " + titular);
        return true;
    }

    public boolean debitar(int numeroConta, double valor, String descricao) {
        ContaBancaria conta = buscarConta(numeroConta);
        if (conta == null) {
            System.out.println("Erro: Conta " + numeroConta + " não encontrada");
            return false;
        }
        
        boolean sucesso = conta.debitarConta(valor, descricao);
        if (sucesso) {
            System.out.println("Débito de R$ " + valor + " realizado com sucesso na conta " + numeroConta);
        } else {
            System.out.println("Erro: Débito de R$ " + valor + " não realizado na conta " + numeroConta);
        }
        return sucesso;
    }

    public void creditar(int numeroConta, double valor, String descricao) {
        ContaBancaria conta = buscarConta(numeroConta);
        if (conta == null) {
            System.out.println("Erro: Conta " + numeroConta + " não encontrada");
            return;
        }
        
        conta.creditarConta(valor, descricao);
        System.out.println("Crédito de R$ " + valor + " realizado com sucesso na conta " + numeroConta);
    }

    public boolean transferir(int numeroContaOrigem, int numeroContaDestino, double valor, String descricao) {
        ContaBancaria contaOrigem = buscarConta(numeroContaOrigem);
        ContaBancaria contaDestino = buscarConta(numeroContaDestino);
        
        if (contaOrigem == null) {
            System.out.println("Erro: Conta origem " + numeroContaOrigem + " não encontrada");
            return false;
        }
        
        if (contaDestino == null) {
            System.out.println("Erro: Conta destino " + numeroContaDestino + " não encontrada");
            return false;
        }
        
        boolean sucesso = contaOrigem.transferirConta(contaDestino, valor, descricao);
        if (sucesso) {
            System.out.println("Transferência de R$ " + valor + " realizada com sucesso da conta " + 
                             numeroContaOrigem + " para conta " + numeroContaDestino);
        } else {
            System.out.println("Erro: Transferência de R$ " + valor + " não realizada");
        }
        return sucesso;
    }

    public void exibirSaldo(int numeroConta) {
        ContaBancaria conta = buscarConta(numeroConta);
        if (conta == null) {
            System.out.println("Erro: Conta " + numeroConta + " não encontrada");
            return;
        }
        
        System.out.println("Saldo da conta " + numeroConta + " (" + conta.getTitular() + "): R$ " + conta.getSaldo());
    }

    public void exibirExtrato(int numeroConta) {
        ContaBancaria conta = buscarConta(numeroConta);
        if (conta == null) {
            System.out.println("Erro: Conta " + numeroConta + " não encontrada");
            return;
        }
        
        System.out.println("=== Extrato da conta " + numeroConta + " (" + conta.getTitular() + ") ===");
        conta.exibirExtrato();
    }

    public void listarContas() {
        System.out.println("=== Lista de Contas do Banco " + nomeBanco + " ===");
        if (contasCadastradas.isEmpty()) {
            System.out.println("Nenhuma conta cadastrada");
            return;
        }
        
        for (ContaBancaria conta : contasCadastradas) {
            String tipoConta = "Normal";
            if (conta instanceof ContaEspecial) {
                tipoConta = "Especial";
            } else if (conta instanceof ContaPoupanca) {
                tipoConta = "Poupança";
            }
            
            System.out.println("Conta " + conta.getNumeroConta() + " - " + conta.getTitular() + 
                             " (" + tipoConta + ") - Saldo: R$ " + conta.getSaldo());
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

    // Getters
    public String getNomeBanco() {
        return nomeBanco;
    }

    public ArrayList<ContaBancaria> getContasCadastradas() {
        return contasCadastradas;
    }

    public int getProximoNumeroConta() {
        return proximoNumeroConta;
    }
}