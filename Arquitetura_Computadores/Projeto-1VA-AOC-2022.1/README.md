# Projeto 1ª VA: VIA-shell em MIPS Assembly

Projeto da disciplina de **Arquitetura e Organização de Computadores** (2022.1), feito em grupo por Vinícius Bezerra, Irlan Farias, Apolo Albuquerque e João Vitor Castro.

O projeto principal é um **shell de linha de comando** (`VIA-shell>>`) escrito em MIPS Assembly para gerenciar os apartamentos de um condomínio: moradores, automóveis e a gravação dos dados em arquivo. Junto dele estão as questões práticas da avaliação.

## Comandos do shell

| Comando | O que faz |
|---|---|
| `ad_morador` | adiciona um morador a um apartamento |
| `rm_morador` | remove um morador |
| `ad_auto` | adiciona um automóvel (carro ou moto, com modelo e cor) |
| `rm_auto` | remove um automóvel |
| `limpar_ap` | esvazia um apartamento |
| `info_ap` | mostra as informações de um apartamento |
| `info_geral` | mostra um resumo geral dos apartamentos |
| `salvar` | salva os dados no arquivo `C:/aps.txt` |
| `recarregar` | recarrega os dados do arquivo |
| `formatar` | apaga os dados de todos os apartamentos (na memória; a gravação só acontece com `salvar`) |

Os argumentos são separados por `-` (por exemplo, `ad_morador-<ap>-<nome>`). O programa valida os comandos e mostra mensagens de erro (apartamento inválido, número máximo de moradores ou automóveis, morador não encontrado etc.).

## Arquivos

| Arquivo / pasta | Conteúdo |
|---|---|
| `final(S_MMIO).asm` | versão mais completa do shell, que lê os comandos pelas syscalls do console (sem MMIO) e implementa todos os comandos da tabela |
| `final.asm` | versão com entrada e saída pelo terminal MMIO (Memory-Mapped I/O); nela, os comandos `salvar`, `recarregar` e `formatar` ainda não foram implementados |
| `Código ASM Projeto/` | versões de cada integrante durante o desenvolvimento |
| `Questões Projeto 1 VA/` | questões práticas: `q1` (substituição de caracteres em string), `q2` (tamanho de uma string), `q3` (Fibonacci), `q4_a` a `q4e` (implementações de `strcpy`, `memcpy`, `strcmp`, `strncmp` e `strcat`) e `q5` (eco de caracteres via MMIO) |

## Como executar

1. Abra o arquivo `.asm` no simulador **MARS**.
2. Monte o código (*Assemble*).
3. Para a versão com MMIO (`final.asm`), abra **Tools → Keyboard and Display MMIO Simulator** e clique em *Connect to MIPS*.
4. Execute (*Run*) e digite os comandos no terminal.

> Os comandos `salvar`, `recarregar` e `formatar` usam o caminho fixo `C:/aps.txt`.

## Tecnologias

MIPS Assembly · MARS · Memory-Mapped I/O
