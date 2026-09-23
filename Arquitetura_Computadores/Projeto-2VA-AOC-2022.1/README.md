# Projeto 2ª VA: Processador MIPS Monociclo em Verilog

Projeto da disciplina de **Arquitetura e Organização de Computadores** (2022.1), feito em grupo por Vinícius Bezerra, Irlan Farias, Apolo Albuquerque e João Vitor Castro.

Implementação de um núcleo **MIPS monociclo** em Verilog HDL, com todos os blocos do caminho de dados e da unidade de controle.

## Módulos

| Arquivo | Módulo |
|---|---|
| `MIPS.v` | top-level que liga todos os blocos (saídas de PC, ULA e memória de dados para visualização) |
| `PC.v` | contador de programa |
| `i_mem.v` | memória de instruções (carrega o `instruction.list`) |
| `regfile.v` | banco de registradores |
| `control.v` | unidade de controle |
| `ula_ctrl.v` | controle da ULA |
| `ula.v` | unidade lógica e aritmética |
| `d_mem.v` | memória de dados |
| `extensor_de_sinal.v` | extensor de sinal de 16 para 32 bits |
| `somadorPC.v` | somador do PC (PC + 4) |
| `somador_jump.v` | somador do endereço de desvio |

## Instruções suportadas

- **Tipo R:** `add`, `sub`, `and`, `or`, `xor`, `nor`, `slt`, `sltu`, `sll`, `srl`, `sra`, `sllv`, `srlv`, `srav`
- **Tipo I:** `addi`, `slti`, `sltiu`, `andi`, `ori`, `xori`, `lw`, `sw`
- **Desvios:** `beq`, `bne`

## Como simular

O arquivo `instruction.list` traz um programa de teste em binário, com uma instrução por linha, que é carregado na memória de instruções.

Para simular, abra o projeto num simulador de Verilog (como ModelSim ou Quartus), defina o `MIPS.v` como top-level e gere os sinais de `clock` e `reset`.

## Tecnologias

Verilog HDL
