# Monitoria de Programação II: Exemplos em Java

Material que preparei como monitor de **Introdução à Programação II**. São exemplos de orientação a objetos em Java, usados nas aulas de monitoria e nas correções das atividades.

## Exemplos

### Sistema Bancário

- **`ContaBancaria`**: número da conta, titular, saldo e histórico de transações, com os métodos `creditarConta`, `debitarConta`, `transferirConta` e `exibirExtrato`.
- **`ContaEspecial`**: herda de `ContaBancaria` e permite ficar negativo até um limite, com taxa de manutenção.
- **`ContaPoupanca`**: herda de `ContaBancaria` e tem aplicação de rendimento.
- **`Banco`**: gerencia as contas.

### Biblioteca

- **`Biblioteca`**: cadastro de livros e revistas, empréstimo e devolução de itens, e listagem do acervo e dos itens disponíveis.
- **`Livro`** e **`Revista`**: os tipos de item do acervo.

## Estrutura

```
ProgII/Java/
├── PropostaLista.zip          # cópia compactada do projeto base
└── JavaProgII/                # projeto Eclipse
    ├── src/                   # exemplos Banco e Biblioteca usados em aula
    ├── Banco/                 # projeto separado do banco, com ContaEspecial e ContaPoupanca
    └── correcaoAtts/          # correção das atividades, com ContaEspecial, ContaPoupanca
                               # e as classes de teste TesteSistemaBancario e TesteBiblioteca
```

## Como executar

Importe a pasta `Java/JavaProgII` no **Eclipse** (*File → Import → Existing Projects into Workspace*) e rode a classe `Main` do exemplo desejado.

## Tecnologias

Java · Eclipse
