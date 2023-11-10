// Projeto 2 VA Arquitetura e Organização de Computadores - 2022.1
// Alunos: Vinícius Bezerra, Irlan Farias, Apolo Albuquerque, joão vitor castro
// Descrição do arquivo: Unidade lógica e aritmética (ula)

module ula (
    input wire [31:0] In1,
    input wire [31:0] In2,
    input wire [3:0] OP,
	 input wire [4:0] shamt,
    output reg Zero_flag,
    output reg [31:0] result
);

	always @(*) begin
		 case (OP)
			  4'b0000: result <= In1 & In2; //and
			  4'b0001: result <= In1 | In2; //or
			  4'b0010: result <= In1 + In2; //soma
			  4'b0011: result <= In1 << In2; //Shift Left Logical Variable
			  4'b0100: result <= In1 >> In2; //Shift Right Logical Variable
			  4'b0101: result <= $signed(In1) >> $signed(In2); //Shift Right Arithmetic Variable
			  4'b0110: result <= In1 - In2; //sub
			  4'b0111: result <=  ($signed(In1) < $signed(In2)) ? 32'b00000000000000000000000000000001 : 32'b00000000000000000000000000000000; //slt			  
			  4'b1000: result <= In1 - In2; //caso especial para bne 
			  4'b1001: result <= In1 << shamt; //Shift Left logico com shamt
			  4'b1010: result <= In1 >> shamt; //Shift Right logico com shamt
			  4'b1011: result <= In1 ^ In2; //xor
			  4'b1100: result <= ~(In1 | In2); //nor
			  4'b1101: result <= $signed(In1) >> shamt; //Shift Right Arithmetic com shamt
			  4'b1111: result <= (In1 < In2) ? 32'b00000000000000000000000000000001 : 32'b00000000000000000000000000000000 ; //sltu    	
			  default: result <= 0;
		 endcase
		 
		 if (result == 0 || OP == 4'h8 & result != 0) begin
			  Zero_flag = 1'b1;
		 end else begin
			  Zero_flag = 1'b0;
		 end
	end

endmodule 