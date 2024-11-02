// Projeto 2 VA Arquitetura e Organização de Computadores - 2022.1
// Alunos: Vinícius Bezerra, Irlan Farias, Apolo Albuquerque, João Vitor Castro
// Descrição do arquivo: Contador de Programa (PC)

module PC (clock, nextPC, PC); // Recebe clock e o endereço da próxima instrução como entrada e retorna um novo endereço.
	
	input wire clock;
	input wire [31:0] nextPC; // Endereço de entrada
	output reg [31:0] PC; // Endereço de saída

	always @(posedge clock) begin
		 PC <= nextPC; // Na subida do clock, transfere o valor de nextPC para PC
	end

endmodule 
