public class TesteSistemaBancario {
    public static void main(String[] args) {
        Banco banco = new Banco("Banco Nova Era");

        banco.criaContaNormal(1001, "Sofia", 1000);
        banco.criaContaEspecial(1002, "Paloma", 500, 300);
        banco.criaContaPoupanca(1003, "Roberta", 2000, 0.02);

        banco.creditar(1001, 300, "Depósito salário");
        banco.debitar(1002, 600, "Compra no cartão");
        banco.transferir(1001, 1003, 200, "Ajuda familiar");

        banco.exibirExtrato(1001);
        banco.exibirExtrato(1002);
        banco.exibirExtrato(1003);

        banco.listarContas();
    }
}
