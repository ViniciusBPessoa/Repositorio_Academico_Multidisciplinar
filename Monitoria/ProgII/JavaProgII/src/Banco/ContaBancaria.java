package Banco;

public class ContaBancaria {
	private int numeroConta;
	private String titular;
	private Double saldo;
	
	public ContaBancaria(int numeroConta, String titular) {
		this.numeroConta = numeroConta;
		this.titular = titular;
		this.saldo = 0.0;
	}
	
	

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
	
	
}
