// Projeto 2 VA Arquitetura e Organização de Computadores - 2022.1
// Alunos: Vinícius Bezerra, Irlan Farias, Apolo Albuquerque, joão vitor castro
// Descrição do arquivo: Somador de 32 bits com entrada soma_pc e ex_pc, e saída po_jp

module somador_jump (soma_pc, ex_pc, po_jp);
	
	// Declara entradas e saídas
	input wire [31:0] soma_pc, ex_pc;
	output wire [31:0] po_jp;

	// Somador de 32 bits com entrada soma_pc e ex_pc, e saída po_jp
	assign po_jp = soma_pc + ex_pc;					// Soma entre 'soma_pc' e 'ex_pc' guardada em 'po_jp'
	
endmodule  
