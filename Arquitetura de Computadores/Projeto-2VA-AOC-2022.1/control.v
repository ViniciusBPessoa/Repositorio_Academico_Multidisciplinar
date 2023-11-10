// Projeto 2 VA Arquitetura e Organização de Computadores - 2022.1
// Alunos: Vinícius Bezerra, Irlan Farias, Apolo Albuquerque, joão vitor castro
// Descrição do arquivo: Unidade de Controle (control))

module control(opcode, RegDst, Branch, ALUSrc, MemWrite, MemRead, MentoReg, ALUOp, RegWrite);

	//Declara entradas e saídas

	input wire [5:0] opcode;
	output reg RegDst;
	output reg Branch;
	output reg ALUSrc;
	output reg MemWrite;
	output reg MemRead;
	output reg MentoReg;
	output reg RegWrite;
	output reg [3:0] ALUOp;

	always @ (opcode) begin						// Sensível a mudança de opcode
		
		case (opcode)

			// Saídas de acordo com entrada em 'opcode'

			6'b000000: begin					// Instruções do tipo R
				RegDst <= 1;
				Branch <= 0;
				ALUSrc <= 0;
				MemWrite <= 0;
				MemRead <= 0;
				MentoReg <= 0;
				RegWrite <= 1;
				ALUOp <= 4'b0000;
				end
			6'b000100: begin					// beq
				RegDst <= 0;
				Branch <= 1;
				ALUSrc <= 0;
				MemWrite <= 0;
				MemRead <= 0;
				MentoReg <= 0;
				RegWrite <= 0;
				ALUOp <= 4'b0100;
				end
			6'b000101: begin					// bne
				RegDst <= 0;
				Branch <= 1;
				ALUSrc <= 0;
				MemWrite <= 0;
				MemRead <= 0;
				MentoReg <= 0;
				RegWrite <= 0;
				ALUOp <= 4'b0101;
				end
			6'b001000: begin					// addi
				RegDst <= 1;
				Branch <= 0;
				ALUSrc <= 1;
				MemWrite <= 0;
				MemRead <= 0;
				MentoReg <= 0;
				RegWrite <= 1;
				ALUOp <= 4'b1000;
				end
			6'b001010: begin					// slti
				RegDst <= 1;
				Branch <= 0;
				ALUSrc <= 1;
				MemWrite <= 0;
				MemRead <= 0;
				MentoReg <= 0;
				RegWrite <= 1;
				ALUOp <= 4'b1010;
				end
			6'b001011: begin					// sltiu
				RegDst <= 1;
				Branch <= 0;
				ALUSrc <= 1;
				MemWrite <= 0;
				MemRead <= 0;
				MentoReg <= 0;
				RegWrite <= 1;
				ALUOp <= 4'b1011;
				end
			6'b001100: begin					// andi
				RegDst <= 1;
				Branch <= 0;
				ALUSrc <= 1;
				MemWrite <= 0;
				MemRead <= 0;
				MentoReg <= 0;
				RegWrite <= 1;
				ALUOp <= 4'b1100;
				end
			6'b001101: begin					// ori		
				RegDst <= 1;
				Branch <= 0;
				ALUSrc <= 1;
				MemWrite <= 0;
				MemRead <= 0;
				MentoReg <= 0;
				RegWrite <= 1;
				ALUOp <= 4'b1101;
				end
			6'b001110: begin					// xori
				RegDst <= 1;
				Branch <= 0;
				ALUSrc <= 1;
				MemWrite <= 0;
				MemRead <= 0;
				MentoReg <= 0;
				RegWrite <= 1;
				ALUOp <= 4'b1110;
				end
			6'b100011: begin					// lw
				RegDst <= 0;
				Branch <= 0;
				ALUSrc <= 1;
				MemWrite <= 0;
				MemRead <= 1;
				MentoReg <= 1;
				RegWrite <= 1;
				ALUOp <= 4'b0000;
				end
			6'b101011: begin					// sw
				RegDst <= 0;
				Branch <= 0;
				ALUSrc <= 1;
				MemWrite <= 1;
				MemRead <= 0;
				MentoReg <= 0;
				RegWrite <= 0;
				ALUOp <= 4'b0000;
				end
			
		endcase
		
	end
	
endmodule 