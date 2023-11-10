// Projeto 2 VA Arquitetura e Organização de Computadores - 2022.1
// Alunos: Vinícius Bezerra, Irlan Farias, Apolo Albuquerque, joão vitor castro
// Descrição do arquivo: Banco de registradores (regfile)

module regfile (ReadAddr1, ReadAddr2 , ReadData1, ReadData2, Clock, WriteAddr, WriteData, RegWrite, Reset);// banco de registradores
	// todos esses inputs e outputs estão explicadas na questão 
	
	input wire [4:0] ReadAddr1, ReadAddr2, WriteAddr; // como a entrada tem 5 bits um total de 32 registradores podem ser utilizados
 	input wire Clock;
	input wire [31:0] WriteData;
	input wire RegWrite, Reset;
	output wire [31:0] ReadData1; 
	output wire [31:0] ReadData2;

	reg [31:0] registradores [0:31]; // cria os 32 registradores 
	integer i; // em caso de reset o i é o controlador de convenções para 0 nos 32 registradores
	
	always @ (posedge Clock or posedge Reset) begin // caso síncrono sensível a clock e reset quando em transição para 1
	
		if (Reset) begin // em caso de reset resetar
			 for (i = 0; i < 32; i = i + 1) begin // percorre os registradores para 0
				registradores[i] <= 32'b0;
			 end
		end 
		else if (Clock) begin
			if(RegWrite != 1'b0 && WriteAddr != 5'b0) begin // em caso de escrita só será liberado em caso de clock e alterações em RegWrite ou WriteAddr
				 registradores[WriteAddr] <= WriteData; // escreve na memória
			end
		end
	end
	
	assign ReadData1 = (ReadAddr1 == 5'b0) ? 32'b0 : registradores[ReadAddr1]; // de forma assincrona carrega ReadData1
   assign ReadData2 = (ReadAddr2 == 5'b0) ? 32'b0 : registradores[ReadAddr2]; // de forma assincrona carrega ReadData1
endmodule  
