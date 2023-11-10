// Projeto 2 VA Arquitetura e Organização de Computadores - 2022.1
// Alunos: Vinícius Bezerra, Irlan Farias, Apolo Albuquerque, joão vitor castro
// Descrição do arquivo: Memória de dados (d_mem)

module d_mem(Address, WriteData, ReadData, MemWrite, MemRead);
	
	input wire [31:0] Address, WriteData; // endereço e a mensagem que será escrita na memória caso o MemWrite seja = 1 
	input wire MemWrite, MemRead;  // verifica se a função é de escrita ou leitura
	output reg [31:0] ReadData; // retorno da leitura
	
	parameter MEM_SIZE = 1024; // memória em si, nesse caso são 1024 posições de 32 bits = 1024 * 32 = 32768 bits ou 4 KiB 
	reg [31:0] memoria [0 : MEM_SIZE-1];// memória em si, nesse caso são 1024 posições de 32 bits = 1024 * 32 = 32768 bits ou 4 KiB 
	assign cabo = Address % MEM_SIZE;
	
	always @ * begin // em qualquer alteração no cabeçalho o valor será retornado 
	
		ReadData = memoria[cabo];  // independente da função ele retorna o valor no local 

		if (MemWrite) begin // caso seja do tipo escrita escreve o valor na memória 
			memoria[cabo] <= WriteData;
		end
	end

endmodule 
